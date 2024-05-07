import fitz
import re
import io
import base64

def highlight_entire_text_on_page(pdf_bytes, page_number, text, color=(1, 0, 0), opacity=1.0):
    try:
        # Open the PDF
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        
        # Ensure the page number is valid
        if page_number > len(doc) or page_number < 1:
            return None, "Page number out of range."    

        try:
            page = doc[page_number - 1]  # Index starts at zero
        except IndexError:
            return None, f"Page {page_number} does not exist in the PDF"

        text_instances = page.search_for(text)
        if len(text_instances) == 0:
            return None, "No matching text found on the page"

        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.update(fill_color=color, opacity=opacity)

        # Render the page with highlights
        pix = page.get_pixmap()
        img_buffer = pix.tobytes("png")    
        
        # Encode the image data buffer as base64
        image_data_base64 = base64.b64encode(img_buffer).decode('utf-8')

        # Save the modified PDF with highlights
        return image_data_base64, None
    except Exception as e:
        return None, f"Error processing PDF: {str(e)}"
# Example usage
#highlighted_image_path = highlight_entire_text_on_page("example.pdf", 2, "Modern computers are designed with the need of high­level languages in mind. The most important technique for structuring programs introduced by high­level languages is the procedure or function. From one point of view, a procedure call alters the flow of control just as a jump does, but unlike a jump, when finished performing its task, a function returns control to the statement or instruction following the call. This high­level abstraction is implemented with the help of the stack. The stack is also used to dynamically allocate the local variables used in func")
#print("Highlighted:", highlighted_image_path)

