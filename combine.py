

# import cv2
# import pytesseract
# import os
# import csv
# import numpy as np

# # Functions for certificate processing
# def preprocess_certificate_image(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     return gray

# def enhance_certificate_underlines(image):
#     blurred = cv2.GaussianBlur(image, (5, 5), 0)
#     adaptive_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#     return adaptive_thresh

# def remove_certificate_noise(image):
#     kernel = np.ones((2, 2), np.uint8)
#     cleaned = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=1)
#     return cleaned

# def detect_certificate_horizontal_lines(image):
#     horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
#     detect_horizontal = cv2.morphologyEx(image, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
#     closing_kernel = np.ones((5, 5), np.uint8)
#     detect_horizontal = cv2.morphologyEx(detect_horizontal, cv2.MORPH_CLOSE, closing_kernel, iterations=2)
#     return detect_horizontal

# def filter_certificate_lines(image, contours, image_height, image_width):
#     filtered_contours = []
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         aspect_ratio = w / float(h)
#         if 89 <= w < image_width - 20 and y > 20 and y < image_height - 20 and aspect_ratio > 5:
#             roi_below = image[y + h:y + h + 30, x:x + w]
#             text_below = pytesseract.image_to_string(roi_below, config='--psm 6').strip()
#             if not text_below:
#                 filtered_contours.append(contour)
#     return filtered_contours

# def extract_certificate_text_from_regions(image, contours, output_folder):
#     underlined_text = []
#     contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[1])  # Sort contours from top to bottom
#     for i, contour in enumerate(contours):
#         x, y, w, h = cv2.boundingRect(contour)
#         if w >= 89:
#             roi_above = image[max(0, y-60):y, x:x+w]  # Increase the height to capture more text
#             text = pytesseract.image_to_string(roi_above, config='--psm 6')
#             if text.strip():
#                 underlined_text.append(text.strip())
#                 # Save image with bounding box
#                 text_region_image = image.copy()
#                 cv2.rectangle(text_region_image, (x, max(0, y-60)), (x + w, y), (255, 0, 0), 2)  # Draw bounding box for the text above the line
#                 cv2.rectangle(text_region_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw bounding box for the underline
#                 cv2.imwrite(os.path.join(output_folder, f'text_region_with_bbox_{i}.png'), text_region_image)  # Save the region above the underline
#     return underlined_text

# def detect_certificate_and_draw_boxes(image, label_text):
#     custom_config = r'--oem 3 --psm 6'
#     data = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
#     n_boxes = len(data['level'])
#     extracted_text = None
#     for i in range(n_boxes):
#         text = data['text'][i].strip()
#         if label_text.lower() in text.lower():
#             (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#             cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
#             # Now detect the text next to the label
#             (x_val, y_val, w_val, h_val) = (data['left'][i + 1], data['top'][i + 1], data['width'][i + 1], data['height'][i + 1])
#             cv2.rectangle(image, (x_val, y_val), (x_val + w_val, y_val + h_val), (255, 0, 0), 2)
#             cv2.putText(image, data['text'][i + 1], (x_val, y_val - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
#             extracted_text = data['text'][i + 1]
#             break

#     return image, extracted_text

# def process_certificate(image_path, output_folder, csv_path):
#     headers = ['Full Name', 'School Name', 'City', 'Exam Year', 'GPA', 'Date of Birth', 'Symbol No.', 'Date of Issue',
#                'Nepali', 'English', 'Maths', 'Science', 'Social', 'Opt-I Mathematics', 'Opt-II Science']
    
#     image = cv2.imread(image_path)
#     preprocessed = preprocess_certificate_image(image)
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#     cv2.imwrite(os.path.join(output_folder, 'preprocessed_image.png'), preprocessed)

#     enhanced_image = enhance_certificate_underlines(preprocessed)
#     cv2.imwrite(os.path.join(output_folder, 'enhanced_image.png'), enhanced_image)

#     cleaned_image = remove_certificate_noise(enhanced_image)
#     cv2.imwrite(os.path.join(output_folder, 'cleaned_image.png'), cleaned_image)

#     detected_horizontal = detect_certificate_horizontal_lines(cleaned_image)
#     cv2.imwrite(os.path.join(output_folder, 'horizontal_lines.png'), detected_horizontal)

#     contours, _ = cv2.findContours(detected_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     filtered_contours = filter_certificate_lines(preprocessed, contours, preprocessed.shape[0], preprocessed.shape[1])

#     underlined_texts = extract_certificate_text_from_regions(preprocessed, filtered_contours, output_folder)
    
#     # Initialize data dictionary for storing extracted texts
#     data = {header: '' for header in headers}  # Initialize with all headers

#     # Save the underlined texts to their respective CSV files
#     for i, text in enumerate(underlined_texts):
#         header = headers[i] if i < len(headers) else f'Header_{i+1}'
#         data[header] = text

#     # Extract specific labeled texts
#     symbol_image, symbol_text = detect_certificate_and_draw_boxes(preprocessed.copy(), 'No.:')
#     cv2.imwrite(os.path.join(output_folder, 'symbol_no.png'), symbol_image)
#     data['Symbol No.'] = symbol_text

#     date_image, date_text = detect_certificate_and_draw_boxes(preprocessed.copy(), 'Issue:')
#     cv2.imwrite(os.path.join(output_folder, 'date_of_issue.png'), date_image)
#     data['Date of Issue'] = date_text

#     write_to_csv(data, headers, csv_path, mode='w')
#     return data

# def validate_marksheet_against_certificate(marksheet_image_path, certificate_data):
#     image = cv2.imread(marksheet_image_path)
#     preprocessed_image = preprocess_marksheet_image(image)
#     custom_config = r'--oem 3 --psm 6'
#     extracted_text = pytesseract.image_to_string(preprocessed_image, config=custom_config)

#     # Print the extracted text for debugging
#     print("Extracted text from marksheet for validation:")
#     print(extracted_text)

#     for key in ['Full Name', 'Symbol No.', 'Date of Birth']:
#         if certificate_data[key].lower() not in extracted_text.lower():
#             print(f"Validation failed: {key} '{certificate_data[key]}' not found in marksheet.")
#             return False
#     return True

# # Functions for marksheet processing
# def preprocess_marksheet_image(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#     adaptive_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 15)
#     return adaptive_thresh

# def visualize_ocr_marksheet_data(image, output_path):
#     custom_config = r'--oem 3 --psm 6'
#     d = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
#     n_boxes = len(d['level'])
#     for i in range(n_boxes):
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     cv2.imwrite(output_path, image)

# def find_marksheet_header_contours(image, header_text):
#     custom_config = r'--oem 3 --psm 6'
#     d = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
#     n_boxes = len(d['level'])
#     for i in range(n_boxes):
#         if header_text.lower() in d['text'][i].lower():
#             (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#             return (x, y, w, h)
#     return None

# def extract_marksheet_texts_from_column(image, header_contour, output_folder, column_name):
#     x, y, w, h = header_contour
#     roi = image[y + h + 10:y + h + 1000, x:x + w]
#     custom_config = r'--oem 3 --psm 6'
#     d = pytesseract.image_to_data(roi, config=custom_config, output_type=pytesseract.Output.DICT)
#     n_boxes = len(d['level'])
#     texts = []
#     for i in range(n_boxes):
#         if int(d['conf'][i]) > 60:
#             (tx, ty, tw, th) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#             text = d['text'][i].strip()
#             if 1 <= len(text) <= 2:
#                 texts.append(text)
#                 cv2.rectangle(image, (x + tx, y + h + 10 + ty), (x + tx + tw, y + h + 10 + ty + th), (0, 255, 0), 2)
#     cv2.imwrite(os.path.join(output_folder, f'{column_name}_bounding_boxes.png'), image)
#     return texts

# def correct_marksheet_ocr_errors(texts):
#     corrected_texts = []
#     for text in texts:
#         corrected_text = text.replace('t', '+')
#         corrected_texts.append(corrected_text)
#     return corrected_texts

# def write_to_csv(data, headers, output_path, mode='a'):
#     with open(output_path, mode, newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=headers)
#         if file.tell() == 0:
#             writer.writeheader()
#         writer.writerow(data)

# def process_marksheet(image_path, output_folder, csv_path, certificate_data):
#     marksheet_headers = ['Nepali', 'English', 'Maths', 'Science', 'Social', 'Opt-I Mathematics', 'Opt-II Science']
#     combined_headers = list(certificate_data.keys()) + marksheet_headers
    
#     image = cv2.imread(image_path)
#     preprocessed_image = preprocess_marksheet_image(image)

#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     cv2.imwrite(os.path.join(output_folder, 'preprocessed_image.png'), preprocessed_image)

#     # Visualize OCR data for debugging
#     ocr_visualization_image = preprocessed_image.copy()
#     visualize_ocr_marksheet_data(ocr_visualization_image, os.path.join(output_folder, 'ocr_visualization.png'))

#     final_grade_header = find_marksheet_header_contours(preprocessed_image, 'FINAL')
#     if not final_grade_header:
#         print("No 'FINAL' header found.")
#         return

#     final_grades_image = image.copy()
#     final_grades = extract_marksheet_texts_from_column(final_grades_image, final_grade_header, output_folder, 'final_grades')

#     corrected_final_grades = correct_marksheet_ocr_errors(final_grades)
#     print("Extracted Final Grades:", corrected_final_grades)

#     cv2.imwrite(os.path.join(output_folder, 'final_grades_contours.png'), final_grades_image)

#     # Create a combined data dictionary that includes both certificate data and marksheet data
#     combined_data = certificate_data.copy()
#     for i, header in enumerate(marksheet_headers):
#         combined_data[header] = corrected_final_grades[i] if i < len(corrected_final_grades) else ''

#     write_to_csv(combined_data, combined_headers, csv_path, mode='w')  # Overwrite the file to update the row

# if __name__ == "__main__":
#     # CSV file path
#     output_csv_path = 'combined_results.csv'

#     # Process certificate
#     certificate_image_path = 'uploads/fake_certificate.png'  # Replace with your certificate image path
#     certificate_output_folder = 'certificate_result'
#     certificate_data = process_certificate(certificate_image_path, certificate_output_folder, output_csv_path)

#     # Validate marksheet against certificate
#     marksheet_image_path = 'uploads/fake_doc.jpg'  # Replace with your marksheet image path
#     if validate_marksheet_against_certificate(marksheet_image_path, certificate_data):
#         # Process marksheet only if validation is successful
#         marksheet_output_folder = 'mark_images'
#         process_marksheet(marksheet_image_path, marksheet_output_folder, output_csv_path, certificate_data)
#     else:
#         print("Marksheet validation failed against certificate. Process stopped.")
import cv2
import pytesseract
import os
import csv
import numpy as np

# Functions for certificate processing
def preprocess_certificate_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def enhance_certificate_underlines(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    adaptive_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    return adaptive_thresh

def remove_certificate_noise(image):
    kernel = np.ones((2, 2), np.uint8)
    cleaned = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=1)
    return cleaned

def detect_certificate_horizontal_lines(image):
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    detect_horizontal = cv2.morphologyEx(image, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    closing_kernel = np.ones((5, 5), np.uint8)
    detect_horizontal = cv2.morphologyEx(detect_horizontal, cv2.MORPH_CLOSE, closing_kernel, iterations=2)
    return detect_horizontal

def filter_certificate_lines(image, contours, image_height, image_width):
    filtered_contours = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if 89 <= w < image_width - 20 and y > 20 and y < image_height - 20 and aspect_ratio > 5:
            roi_below = image[y + h:y + h + 30, x:x + w]
            text_below = pytesseract.image_to_string(roi_below, config='--psm 6').strip()
            if not text_below:
                filtered_contours.append(contour)
    return filtered_contours

def extract_certificate_text_from_regions(image, contours, output_folder):
    underlined_text = []
    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[1])  # Sort contours from top to bottom
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if w >= 89:
            roi_above = image[max(0, y-60):y, x:x+w]  # Increase the height to capture more text
            text = pytesseract.image_to_string(roi_above, config='--psm 6')
            if text.strip():
                underlined_text.append(text.strip())
                # Save image with bounding box
                text_region_image = image.copy()
                cv2.rectangle(text_region_image, (x, max(0, y-60)), (x + w, y), (255, 0, 0), 2)  # Draw bounding box for the text above the line
                cv2.rectangle(text_region_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw bounding box for the underline
                cv2.imwrite(os.path.join(output_folder, f'text_region_with_bbox_{i}.png'), text_region_image)  # Save the region above the underline
    return underlined_text

def detect_certificate_and_draw_boxes(image, label_text):
    custom_config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
    n_boxes = len(data['level'])
    extracted_text = None
    for i in range(n_boxes):
        text = data['text'][i].strip()
        if label_text.lower() in text.lower():
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            # Now detect the text next to the label
            (x_val, y_val, w_val, h_val) = (data['left'][i + 1], data['top'][i + 1], data['width'][i + 1], data['height'][i + 1])
            cv2.rectangle(image, (x_val, y_val), (x_val + w_val, y_val + h_val), (255, 0, 0), 2)
            cv2.putText(image, data['text'][i + 1], (x_val, y_val - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            extracted_text = data['text'][i + 1]
            break

    return image, extracted_text

def process_certificate(image_path, output_folder, csv_path):
    headers = ['Full_Name', 'School_Name', 'City', 'Exam_Year', 'GPA', 'Date_of_Birth', 'Symbol_No', 'Date_of_Issue',
               'Nepali', 'English', 'Maths', 'Science', 'Social', 'Opt_I_Mathematics', 'Opt_II_Science']
    
    image = cv2.imread(image_path)
    preprocessed = preprocess_certificate_image(image)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    cv2.imwrite(os.path.join(output_folder, 'preprocessed_image.png'), preprocessed)

    enhanced_image = enhance_certificate_underlines(preprocessed)
    cv2.imwrite(os.path.join(output_folder, 'enhanced_image.png'), enhanced_image)

    cleaned_image = remove_certificate_noise(enhanced_image)
    cv2.imwrite(os.path.join(output_folder, 'cleaned_image.png'), cleaned_image)

    detected_horizontal = detect_certificate_horizontal_lines(cleaned_image)
    cv2.imwrite(os.path.join(output_folder, 'horizontal_lines.png'), detected_horizontal)

    contours, _ = cv2.findContours(detected_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    filtered_contours = filter_certificate_lines(preprocessed, contours, preprocessed.shape[0], preprocessed.shape[1])

    underlined_texts = extract_certificate_text_from_regions(preprocessed, filtered_contours, output_folder)
    
    # Initialize data dictionary for storing extracted texts
    data = {header: '' for header in headers}  # Initialize with all headers

    # Save the underlined texts to their respective CSV files
    for i, text in enumerate(underlined_texts):
        header = headers[i] if i < len(headers) else f'Header_{i+1}'
        data[header] = text

    # Extract specific labeled texts
    symbol_image, symbol_text = detect_certificate_and_draw_boxes(preprocessed.copy(), 'No.:')
    cv2.imwrite(os.path.join(output_folder, 'symbol_no.png'), symbol_image)
    data['Symbol_No'] = symbol_text

    date_image, date_text = detect_certificate_and_draw_boxes(preprocessed.copy(), 'Issue:')
    cv2.imwrite(os.path.join(output_folder, 'date_of_issue.png'), date_image)
    data['Date_of_Issue'] = date_text

    write_to_csv(data, headers, csv_path, mode='w')
    return data

def validate_marksheet_against_certificate(marksheet_image_path, certificate_data):
    image = cv2.imread(marksheet_image_path)
    preprocessed_image = preprocess_marksheet_image(image)
    custom_config = r'--oem 3 --psm 6'
    extracted_text = pytesseract.image_to_string(preprocessed_image, config=custom_config)

    # Print the extracted text for debugging
    print("Extracted text from marksheet for validation:")
    print(extracted_text)

    for key in ['Full_Name', 'Symbol_No', 'Date_of_Birth']:
        if certificate_data[key].lower() not in extracted_text.lower():
            print(f"Validation failed: {key} '{certificate_data[key]}' not found in marksheet.")
            return False
    return True

# Functions for marksheet processing
def preprocess_marksheet_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    adaptive_thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 15)
    return adaptive_thresh

def visualize_ocr_marksheet_data(image, output_path):
    custom_config = r'--oem 3 --psm 6'
    d = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(output_path, image)

def find_marksheet_header_contours(image, header_text):
    custom_config = r'--oem 3 --psm 6'
    d = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        if header_text.lower() in d['text'][i].lower():
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            return (x, y, w, h)
    return None

def extract_marksheet_texts_from_column(image, header_contour, output_folder, column_name):
    x, y, w, h = header_contour
    roi = image[y + h + 10:y + h + 1000, x:x + w]
    custom_config = r'--oem 3 --psm 6'
    d = pytesseract.image_to_data(roi, config=custom_config, output_type=pytesseract.Output.DICT)
    n_boxes = len(d['level'])
    texts = []
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (tx, ty, tw, th) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            text = d['text'][i].strip()
            if 1 <= len(text) <= 2:
                texts.append(text)
                cv2.rectangle(image, (x + tx, y + h + 10 + ty), (x + tx + tw, y + h + 10 + ty + th), (0, 255, 0), 2)
    cv2.imwrite(os.path.join(output_folder, f'{column_name}_bounding_boxes.png'), image)
    return texts

def correct_marksheet_ocr_errors(texts):
    corrected_texts = []
    for text in texts:
        corrected_text = text.replace('t', '+')
        corrected_texts.append(corrected_text)
    return corrected_texts

def write_to_csv(data, headers, output_path, mode='a'):
    with open(output_path, mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

def process_marksheet(image_path, output_folder, csv_path, certificate_data):
    marksheet_headers = ['Nepali', 'English', 'Maths', 'Science', 'Social', 'Opt_I_Mathematics', 'Opt_II_Science']
    combined_headers = list(certificate_data.keys()) + [header for header in marksheet_headers if header not in certificate_data]
    
    image = cv2.imread(image_path)
    preprocessed_image = preprocess_marksheet_image(image)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cv2.imwrite(os.path.join(output_folder, 'preprocessed_image.png'), preprocessed_image)

    # Visualize OCR data for debugging
    ocr_visualization_image = preprocessed_image.copy()
    visualize_ocr_marksheet_data(ocr_visualization_image, os.path.join(output_folder, 'ocr_visualization.png'))

    final_grade_header = find_marksheet_header_contours(preprocessed_image, 'FINAL')
    if not final_grade_header:
        print("No 'FINAL' header found.")
        return

    final_grades_image = image.copy()
    final_grades = extract_marksheet_texts_from_column(final_grades_image, final_grade_header, output_folder, 'final_grades')

    corrected_final_grades = correct_marksheet_ocr_errors(final_grades)
    print("Extracted Final Grades:", corrected_final_grades)

    cv2.imwrite(os.path.join(output_folder, 'final_grades_contours.png'), final_grades_image)

    # Create a combined data dictionary that includes both certificate data and marksheet data
    combined_data = certificate_data.copy()
    for i, header in enumerate(marksheet_headers):
        combined_data[header] = corrected_final_grades[i] if i < len(corrected_final_grades) else ''

    write_to_csv(combined_data, combined_headers, csv_path, mode='w')  # Overwrite the file to update the row

if __name__ == "__main__":
    # CSV file path
    output_csv_path = 'combined_results.csv'

    # Process certificate
    certificate_image_path = 'uploads/fake_certificate.png'  # Replace with your certificate image path
    certificate_output_folder = 'certificate_result'
    certificate_data = process_certificate(certificate_image_path, certificate_output_folder, output_csv_path)

    # Validate marksheet against certificate
    marksheet_image_path = 'uploads/fake_doc.jpg'  # Replace with your marksheet image path
    if validate_marksheet_against_certificate(marksheet_image_path, certificate_data):
        # Process marksheet only if validation is successful
        marksheet_output_folder = 'mark_images'
        process_marksheet(marksheet_image_path, marksheet_output_folder, output_csv_path, certificate_data)
    else:
        print("Marksheet validation failed against certificate. Process stopped.")
