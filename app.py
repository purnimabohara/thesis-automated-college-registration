# from flask import Flask, render_template, request, redirect, send_file, url_for, flash
# import os
# from combine import process_certificate, validate_marksheet_against_certificate, process_marksheet
# from autofill import read_csv_data, save_to_pdf
# from pymongo import MongoClient

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['CERTIFICATES_FOLDER'] = os.path.join(app.config['UPLOAD_FOLDER'], 'certificates')
# app.config['MARKSHEETS_FOLDER'] = os.path.join(app.config['UPLOAD_FOLDER'], 'marksheets')
# app.config['PROCESSED_FOLDER'] = 'processed'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
# app.secret_key = 'supersecretkey'

# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
# if not os.path.exists(app.config['CERTIFICATES_FOLDER']):
#     os.makedirs(app.config['CERTIFICATES_FOLDER'])
# if not os.path.exists(app.config['MARKSHEETS_FOLDER']):
#     os.makedirs(app.config['MARKSHEETS_FOLDER'])
# if not os.path.exists(app.config['PROCESSED_FOLDER']):
#     os.makedirs(app.config['PROCESSED_FOLDER'])

# # Initialize MongoDB client
# client = MongoClient('mongodb://localhost:27017/')
# db = client.college_registration
# students_collection = db.students

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# @app.route('/', methods=['GET', 'POST'])
# def upload_files():
#     student_data = None
#     certificate_path = None
#     marksheet_path = None

#     if request.method == 'POST':
#         if 'certificate' not in request.files or 'marksheet' not in request.files:
#             flash('No file part')
#             return redirect(request.url)

#         certificate = request.files['certificate']
#         marksheet = request.files['marksheet']

#         if certificate.filename == '' or marksheet.filename == '':
#             flash('No selected file')
#             return redirect(request.url)

#         if allowed_file(certificate.filename) and allowed_file(marksheet.filename):
#             certificate_path = os.path.join(app.config['CERTIFICATES_FOLDER'], certificate.filename)
#             marksheet_path = os.path.join(app.config['MARKSHEETS_FOLDER'], marksheet.filename)

#             certificate.save(certificate_path)
#             marksheet.save(marksheet_path)

#             # Process files
#             csv_path = os.path.join(app.config['PROCESSED_FOLDER'], 'combined_results.csv')
#             certificate_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'certificate_result')
#             marksheet_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'mark_images')

#             certificate_data = process_certificate(certificate_path, certificate_output_folder, csv_path)

#             if validate_marksheet_against_certificate(marksheet_path, certificate_data):
#                 process_marksheet(marksheet_path, marksheet_output_folder, csv_path, certificate_data)
                
#                 data = read_csv_data(csv_path)
#                 if data:
#                     student_data = data[0]  # Assuming one student's data per file
#             else:
#                 flash('Marksheet validation failed: The marksheet does not belong to the certificate holder.')
#                 certificate_path = None
#                 marksheet_path = None

#     return render_template('index.html', student_data=student_data, certificate_path=certificate_path, marksheet_path=marksheet_path)

# @app.route('/save', methods=['POST'])
# def save_form():
#     student_data = request.form.to_dict()
#     symbol_no = student_data.get('Symbol_No')

#     if symbol_no:
#         result = students_collection.update_one({'Symbol_No': symbol_no}, {'$set': student_data}, upsert=True)
#         if result.modified_count > 0:
#             flash('Data updated successfully')
#         else:
#             flash('Data saved successfully')
#     else:
#         flash('Error saving data')

#     return render_template('index.html', student_data=student_data)

# @app.route('/download_pdf', methods=['GET'])
# def download_pdf():
#     symbol_no = request.args.get('Symbol_No')

#     if not symbol_no:
#         flash('Symbol number not provided')
#         return redirect(url_for('upload_files'))

#     student_data = students_collection.find_one({'Symbol_No': symbol_no})

#     if not student_data:
#         flash('No data found for the given symbol number')
#         return redirect(url_for('upload_files'))

#     pdf_path = save_to_pdf(student_data)
#     return send_file(pdf_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, session
# import os

# from pymongo import MongoClient
# from combine import process_certificate, validate_marksheet_against_certificate, process_marksheet
# from autofill import read_csv_data, save_to_pdf, save_to_database

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['CERTIFICATES_FOLDER'] = os.path.join(app.config['UPLOAD_FOLDER'], 'certificates')
# app.config['MARKSHEETS_FOLDER'] = os.path.join(app.config['UPLOAD_FOLDER'], 'marksheets')
# app.config['PROCESSED_FOLDER'] = 'processed'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
# app.secret_key = 'supersecretkey'  # Required for flashing messages

# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
# if not os.path.exists(app.config['CERTIFICATES_FOLDER']):
#     os.makedirs(app.config['CERTIFICATES_FOLDER'])
# if not os.path.exists(app.config['MARKSHEETS_FOLDER']):
#     os.makedirs(app.config['MARKSHEETS_FOLDER'])
# if not os.path.exists(app.config['PROCESSED_FOLDER']):
#     os.makedirs(app.config['PROCESSED_FOLDER'])

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# # @app.route('/', methods=['GET', 'POST'])
# # def upload_files():
# #     student_data = None
# #     certificate_path = None
# #     marksheet_path = None

# #     if request.method == 'POST':
# #         if 'certificate' not in request.files or 'marksheet' not in request.files:
# #             flash('No file part')
# #             return redirect(request.url)

# #         certificate = request.files['certificate']
# #         marksheet = request.files['marksheet']

# #         if certificate.filename == '' or marksheet.filename == '':
# #             flash('No selected file')
# #             return redirect(request.url)

# #         if allowed_file(certificate.filename) and allowed_file(marksheet.filename):
# #             certificate_path = os.path.join(app.config['CERTIFICATES_FOLDER'], certificate.filename)
# #             marksheet_path = os.path.join(app.config['MARKSHEETS_FOLDER'], marksheet.filename)

# #             certificate.save(certificate_path)
# #             marksheet.save(marksheet_path)

# #             # Process files
# #             csv_path = os.path.join(app.config['PROCESSED_FOLDER'], 'combined_results.csv')
# #             certificate_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'certificate_result')
# #             marksheet_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'mark_images')

# #             certificate_data = process_certificate(certificate_path, certificate_output_folder, csv_path)

# #             if validate_marksheet_against_certificate(marksheet_path, certificate_data):
# #                 process_marksheet(marksheet_path, marksheet_output_folder, csv_path, certificate_data)
                
# #                 data = read_csv_data(csv_path)
# #                 if data:
# #                     student_data = data[0]  # Assuming one student's data per file
# #             else:
# #                 flash('Marksheet validation failed: The marksheet does not belong to the certificate holder.')
# #                 certificate_path = None
# #                 marksheet_path = None

# #     return render_template('index.html', student_data=student_data, certificate_path=certificate_path, marksheet_path=marksheet_path)
# # @app.route('/', methods=['GET', 'POST'])
# # def upload_files():
# #     student_data = None
# #     certificate_path = None
# #     marksheet_path = None

# #     if request.method == 'POST':
# #         if 'certificate' not in request.files or 'marksheet' not in request.files:
# #             flash('No file part')
# #             return redirect(request.url)

# #         certificate = request.files['certificate']
# #         marksheet = request.files['marksheet']

# #         if certificate.filename == '' or marksheet.filename == '':
# #             flash('No selected file')
# #             return redirect(request.url)

# #         if allowed_file(certificate.filename) and allowed_file(marksheet.filename):
# #             certificate_path = os.path.join(app.config['CERTIFICATES_FOLDER'], certificate.filename)
# #             marksheet_path = os.path.join(app.config['MARKSHEETS_FOLDER'], marksheet.filename)

# #             certificate.save(certificate_path)
# #             marksheet.save(marksheet_path)

# #             # Process files
# #             csv_path = os.path.join(app.config['PROCESSED_FOLDER'], 'combined_results.csv')
# #             certificate_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'certificate_result')
# #             marksheet_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'mark_images')

# #             certificate_data = process_certificate(certificate_path, certificate_output_folder, csv_path)

# #             if validate_marksheet_against_certificate(marksheet_path, certificate_data):
# #                 process_marksheet(marksheet_path, marksheet_output_folder, csv_path, certificate_data)
                
# #                 data = read_csv_data(csv_path)
# #                 if data:
# #                     student_data = data[0]  # Assuming one student's data per file
# #             else:
# #                 flash('Marksheet validation failed: The marksheet does not belong to the certificate holder.')
# #                 certificate_path = None
# #                 marksheet_path = None
# #                 student_data = None  # Ensure the form on the right does not appear

# #     return render_template('index.html', student_data=student_data, certificate_path=certificate_path, marksheet_path=marksheet_path)



from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import os
from pymongo import MongoClient
from bson import ObjectId  # Import to handle ObjectId serialization
from combine import process_certificate, validate_marksheet_against_certificate, process_marksheet
from autofill import read_csv_data, save_to_pdf, save_to_database

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['CERTIFICATES_FOLDER'] = os.path.join(app.config['UPLOAD_FOLDER'], 'certificates')
app.config['MARKSHEETS_FOLDER'] = os.path.join(app.config['UPLOAD_FOLDER'], 'marksheets')
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.secret_key = 'supersecretkey'  # Required for flashing messages

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['CERTIFICATES_FOLDER']):
    os.makedirs(app.config['CERTIFICATES_FOLDER'])
if not os.path.exists(app.config['MARKSHEETS_FOLDER']):
    os.makedirs(app.config['MARKSHEETS_FOLDER'])
if not os.path.exists(app.config['PROCESSED_FOLDER']):
    os.makedirs(app.config['PROCESSED_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Helper function to serialize ObjectId
def serialize_data(data):
    if isinstance(data, list):
        return [serialize_data(item) for item in data]
    if isinstance(data, dict):
        return {key: serialize_data(value) for key, value in data.items()}
    if isinstance(data, ObjectId):
        return str(data)
    return data



@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        if 'certificate' not in request.files or 'marksheet' not in request.files:
            return jsonify({'success': False, 'message': 'No file part'}), 400

        certificate = request.files['certificate']
        marksheet = request.files['marksheet']

        if certificate.filename == '' or marksheet.filename == '':
            return jsonify({'success': False, 'message': 'No selected file'}), 400

        if allowed_file(certificate.filename) and allowed_file(marksheet.filename):
            certificate_path = os.path.join(app.config['CERTIFICATES_FOLDER'], certificate.filename)
            marksheet_path = os.path.join(app.config['MARKSHEETS_FOLDER'], marksheet.filename)

            certificate.save(certificate_path)
            marksheet.save(marksheet_path)

            # Process files
            csv_path = os.path.join(app.config['PROCESSED_FOLDER'], 'combined_results.csv')
            certificate_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'certificate_result')
            marksheet_output_folder = os.path.join(app.config['PROCESSED_FOLDER'], 'mark_images')

            certificate_data = process_certificate(certificate_path, certificate_output_folder, csv_path)

            if validate_marksheet_against_certificate(marksheet_path, certificate_data):
                process_marksheet(marksheet_path, marksheet_output_folder, csv_path, certificate_data)
                
                data = read_csv_data(csv_path)
                if data:
                    student_data = data[0]  # Assuming one student's data per file
                return jsonify({'success': True, 'student_data': serialize_data(student_data)}), 200
            else:
                return jsonify({'success': False, 'message': 'Marksheet validation failed: The marksheet does not belong to the certificate holder.'}), 400

        return jsonify({'success': False, 'message': 'File type not allowed'}), 400

    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_form():
    student_data = request.form.to_dict()
    save_to_database(student_data)
    serialized_data = serialize_data(student_data)
    return jsonify({'success': True, 'message': 'Data saved successfully!', 'student_data': serialized_data}), 200

# @app.route('/download', methods=['GET'])
# def download_pdf():
#     symbol_no = request.args.get('Symbol_No')

#     client = MongoClient("mongodb://localhost:27017/")
#     db = client["college_registration"]
#     collection = db["students"]
#     existing_student = collection.find_one({"Symbol_No": symbol_no})

#     if existing_student:
#         pdf_path = save_to_pdf(existing_student)
#         return jsonify({'success': True, 'pdf_url': url_for('processed', filename=pdf_path.split('/')[-1])}), 200
#     else:
#         return jsonify({'success': False, 'message': 'Data must be saved before downloading the PDF.'}), 400

@app.route('/download', methods=['GET'])
def download_pdf():
    symbol_no = request.args.get('Symbol_No')

    # Ensure the symbol number is correct
    print(f"Symbol Number: {symbol_no}")  

    client = MongoClient("mongodb://localhost:27017/")
    db = client["college_registration"]
    collection = db["students"]
    existing_student = collection.find_one({"Symbol_No": symbol_no})

    # Verify that the correct student data is retrieved
    if existing_student:
        print(f"Existing Student Data: {existing_student}")  # Debugging output

        pdf_path = save_to_pdf(existing_student)
        print(f"Generated PDF Path: {pdf_path}")  # Debugging output

        if pdf_path:
            return jsonify({'success': True, 'pdf_url': url_for('processed', filename=pdf_path.split('/')[-1])}), 200
        else:
            print("PDF generation failed.")  # Debugging output
            return jsonify({'success': False, 'message': 'PDF generation failed.'}), 500
    else:
        print("No matching student found.")  # Debugging output
        return jsonify({'success': False, 'message': 'Data must be saved before downloading the PDF.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
