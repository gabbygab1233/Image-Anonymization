from helpers import convert_and_trim_bb
import streamlit as st 
import warnings
import imutils
import dlib
import cv2
import numpy as np

st.set_page_config(page_title="Image Anonymization", page_icon="🎞", layout='centered', initial_sidebar_state="collapsed")

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:blue;text-align:left;">Image Anonymization 🧿 </h1>
    </div>      
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    '''
    ## How does it work ❓ 
    Upload any picture and it will automatically blur all the faces in the image.
    '''
    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'])
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)

        col_1, col_2 = st.beta_columns(2)
        with col_1:
            # Convert the file to an opencv image.
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)
            image = imutils.resize(opencv_image, width=600)
            col_1.header("Original Image")
            col_1.image(image, channels="BGR",use_column_width=True)
        with col_2:
            detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = detector(rgb, 1)
            face  = [convert_and_trim_bb(image, r.rect) for r in results]
            # loop over the bounding boxes
            for (x, y, w, h) in face:
                # draw the bounding box on our image
                image[y:y+h, x:x+w] = cv2.medianBlur(image[y:y+h, x:x+w], 19)
            col_2.header("Anonymize Image")
            col_2.image(image, channels="BGR",use_column_width=True)

    '''
    [![Github](https://i.ibb.co/vDLv9z9/iconfinder-mark-github-298822-3.png)](https://github.com/gabbygab1233/Image-Anonymization)
    ** Source Code**'''
    

    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
if __name__ == '__main__':
	main()