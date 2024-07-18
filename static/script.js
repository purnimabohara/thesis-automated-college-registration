

// // Function to preview the image and optionally store it in sessionStorage
// function previewImage(input, targetId, nameId) {
//   if (input.files && input.files[0]) {
//       var reader = new FileReader();
//       reader.onload = function (e) {
//           var target = document.getElementById(targetId);
//           target.src = e.target.result;
//           target.style.display = "block"; // Make sure the image is displayed

//           // Display the file name
//           document.getElementById(nameId).textContent = input.files[0].name;
//       };
//       reader.readAsDataURL(input.files[0]); // Read the uploaded file
//   }
// }

// // Event listeners for the file inputs
// document.getElementById("certificate").addEventListener("change", function () {
//   previewImage(this, "certificatePreview", "certificateFileName");
// });

// document.getElementById("marksheet").addEventListener("change", function () {
//   previewImage(this, "marksheetPreview", "marksheetFileName");
// });

// // Handling form submission with progress bar and storing image data in sessionStorage
// document.getElementById('uploadForm').addEventListener('submit', function(event) {
//   event.preventDefault(); // Prevent the form from submitting immediately

//   // Store the image data in sessionStorage just before submitting
//   var certificatePreview = document.getElementById('certificatePreview').src;
//   var marksheetPreview = document.getElementById('marksheetPreview').src;

//   sessionStorage.setItem('certificateImage', certificatePreview);
//   sessionStorage.setItem('marksheetImage', marksheetPreview);

//   // Show the progress bar
//   var progressBar = document.getElementById('progress-bar');
//   var progressContainer = document.querySelector('.progress-container');
//   progressContainer.style.display = 'block';

//   var width = 0;
//   var interval = setInterval(function() {
//       if (width >= 100) {
//           clearInterval(interval);
//           sessionStorage.setItem('formSubmitted', 'true'); // Store the submission flag
//           document.getElementById('uploadForm').submit(); // Submit the form
//       } else {
//           width++;
//           progressBar.style.width = width + '%';
//       }
//   }, 50); // Adjust the speed of the progress bar
// });

// // Check if the form was submitted successfully and show the right section
// if (sessionStorage.getItem('formSubmitted') === 'true') {
//   var certificateImage = sessionStorage.getItem('certificateImage');
//   var marksheetImage = sessionStorage.getItem('marksheetImage');

//   if (certificateImage) {
//       var certificatePreview = document.getElementById('certificatePreview');
//       certificatePreview.src = certificateImage;
//       certificatePreview.style.display = 'block';
//   }

//   if (marksheetImage) {
//       var marksheetPreview = document.getElementById('marksheetPreview');
//       marksheetPreview.src = marksheetImage;
//       marksheetPreview.style.display = 'block';
//   }

//   document.querySelector('.right').style.display = 'block';
//   sessionStorage.removeItem('formSubmitted'); // Clear the flag after handling
// } else {
//   // Clear sessionStorage on a regular page load
//   sessionStorage.removeItem('certificateImage');
//   sessionStorage.removeItem('marksheetImage');
// }
// Function to preview the image and display the file name
// function previewImage(input, targetId, nameId) {
//   if (input.files && input.files[0]) {
//       var reader = new FileReader();
//       reader.onload = function (e) {
//           var target = document.getElementById(targetId);
//           target.src = e.target.result;
//           target.style.display = "block"; 

//           // Display the file name
//           document.getElementById(nameId).textContent = input.files[0].name;
//       };
//       reader.readAsDataURL(input.files[0]); 
//   }
// }


// document.getElementById("certificate").addEventListener("change", function () {
//   previewImage(this, "certificatePreview", "certificateFileName");
// });

// document.getElementById("marksheet").addEventListener("change", function () {
//   previewImage(this, "marksheetPreview", "marksheetFileName");
// });



// function resetFormFields() {
//   document.getElementById('marksheetFileName').textContent = '';
//   document.getElementById('marksheetPreview').style.display = 'none';
//   document.getElementById('marksheetPreview').src = ''; 

//   document.getElementById('certificateFileName').textContent = '';
//   document.getElementById('certificatePreview').style.display = 'none';
//   document.getElementById('certificatePreview').src = ''; 

//   var errorMessages = document.querySelectorAll('.validation-error');
//   errorMessages.forEach(function(message) {
//       message.style.color = 'red';  
//   });
// }


// if (document.querySelector('.validation-error')) {  
//   resetFormFields();
// }



// document.getElementById('uploadForm').addEventListener('submit', function(event) {
//   event.preventDefault();


//   var certificatePreview = document.getElementById('certificatePreview').src;
//   var marksheetPreview = document.getElementById('marksheetPreview').src;

//   sessionStorage.setItem('certificateImage', certificatePreview);
//   sessionStorage.setItem('marksheetImage', marksheetPreview);

//   // Show the progress bar
//   var progressBar = document.getElementById('progress-bar');
//   var progressContainer = document.querySelector('.progress-container');
//   progressContainer.style.display = 'block';

//   var width = 0;
//   var interval = setInterval(function() {
//       if (width >= 100) {
//           clearInterval(interval);
//           sessionStorage.setItem('formSubmitted', 'true'); // Store the submission flag
//           document.getElementById('uploadForm').submit(); // Submit the form
//       } else {
//           width++;
//           progressBar.style.width = width + '%';
//       }
//   }, 50); // Adjust the speed of the progress bar
// });

// // Check if the form was submitted successfully and show the right section
// if (sessionStorage.getItem('formSubmitted') === 'true') {
//   var certificateImage = sessionStorage.getItem('certificateImage');
//   var marksheetImage = sessionStorage.getItem('marksheetImage');

//   if (certificateImage) {
//       var certificatePreview = document.getElementById('certificatePreview');
//       certificatePreview.src = certificateImage;
//       certificatePreview.style.display = 'block';
//   }

//   if (marksheetImage) {
//       var marksheetPreview = document.getElementById('marksheetPreview');
//       marksheetPreview.src = marksheetImage;
//       marksheetPreview.style.display = 'block';
//   }

//   document.querySelector('.right').style.display = 'block';
//   sessionStorage.removeItem('formSubmitted'); // Clear the flag after handling
// } else {
//   // Clear sessionStorage on a regular page load
//   sessionStorage.removeItem('certificateImage');
//   sessionStorage.removeItem('marksheetImage');
// }

// // If the form was reloaded due to validation failure, reset the form fields
// if (document.querySelector('.right') === null) {
//   resetFormFields();
// }
// document.addEventListener('DOMContentLoaded', function() {
//   var certificateInput = document.getElementById("certificate");
//   var marksheetInput = document.getElementById("marksheet");

//   if (certificateInput) {
//       certificateInput.addEventListener("change", function () {
//           previewImage(this, "certificatePreview", "certificateFileName");
//       });
//   }

//   if (marksheetInput) {
//       marksheetInput.addEventListener("change", function () {
//           previewImage(this, "marksheetPreview", "marksheetFileName");
//       });
//   }
// });

// function previewImage(input, targetId, nameId) {
//   if (input.files && input.files[0]) {
//       var reader = new FileReader();
//       reader.onload = function (e) {
//           var target = document.getElementById(targetId);
//           target.src = e.target.result;
//           target.style.display = "block"; 

//           // Display the file name
//           document.getElementById(nameId).textContent = input.files[0].name;
//       };
//       reader.readAsDataURL(input.files[0]); 
//   }
// }

// function resetFormFields() {
//   document.getElementById('marksheetFileName').textContent = '';
//   document.getElementById('marksheetPreview').style.display = 'none';
//   document.getElementById('marksheetPreview').src = ''; 
// }

// if (document.querySelector('.validation-error')) {  
//   resetFormFields();
// }

// document.getElementById('uploadForm').addEventListener('submit', function(event) {
//   event.preventDefault();

//   var certificatePreview = document.getElementById('certificatePreview').src;
//   var marksheetPreview = document.getElementById('marksheetPreview').src;

//   sessionStorage.setItem('certificateImage', certificatePreview);
//   sessionStorage.setItem('marksheetImage', marksheetPreview);

//   // Show the progress bar
//   var progressBar = document.getElementById('progress-bar');
//   var progressContainer = document.querySelector('.progress-container');
//   progressContainer.style.display = 'block';

//   var width = 0;
//   var interval = setInterval(function() {
//       if (width >= 100) {
//           clearInterval(interval);
//           sessionStorage.setItem('formSubmitted', 'true'); // Store the submission flag
//           document.getElementById('uploadForm').submit(); // Submit the form
//       } else {
//           width++;
//           progressBar.style.width = width + '%';
//       }
//   }, 50); // Adjust the speed of the progress bar
// });

// // Check if the form was submitted successfully and show the right section
// if (sessionStorage.getItem('formSubmitted') === 'true') {
//   var certificateImage = sessionStorage.getItem('certificateImage');
//   var marksheetImage = sessionStorage.getItem('marksheetImage');

//   if (certificateImage) {
//       var certificatePreview = document.getElementById('certificatePreview');
//       certificatePreview.src = certificateImage;
//       certificatePreview.style.display = 'block';
//   }

//   if (marksheetImage) {
//       var marksheetPreview = document.getElementById('marksheetPreview');
//       marksheetPreview.src = marksheetImage;
//       marksheetPreview.style.display = 'block';
//   }

//   document.querySelector('.right').style.display = 'block';
//   sessionStorage.removeItem('formSubmitted'); // Clear the flag after handling
// } else {
//   // Clear sessionStorage on a regular page load
//   sessionStorage.removeItem('certificateImage');
//   sessionStorage.removeItem('marksheetImage');
// }

// // If the form was reloaded due to validation failure, reset the form fields
// if (document.querySelector('.right') === null) {
//   resetFormFields();
// }
$(document).ready(function () {
  // Handle file inputs and preview
  var certificateInput = document.getElementById("certificate");
  var marksheetInput = document.getElementById("marksheet");

  if (certificateInput) {
      certificateInput.addEventListener("change", function () {
          previewImage(this, "certificatePreview", "certificateFileName");
      });
  }

  if (marksheetInput) {
      marksheetInput.addEventListener("change", function () {
          previewImage(this, "marksheetPreview", "marksheetFileName");
      });
  }

  // Handle form submission for file upload with progress bar
  $("#uploadForm").on("submit", function (event) {
      event.preventDefault();

      var formData = new FormData(this);

      // Store the previewed images in sessionStorage before submission
      var certificatePreview = document.getElementById('certificatePreview').src;
      var marksheetPreview = document.getElementById('marksheetPreview').src;

      sessionStorage.setItem('certificateImage', certificatePreview);
      sessionStorage.setItem('marksheetImage', marksheetPreview);

      // Show the progress bar
      var progressBar = document.getElementById('progress-bar');
      var progressContainer = document.querySelector('.progress-container');
      progressContainer.style.display = 'block';

      var width = 0;
      var interval = setInterval(function() {
          if (width >= 100) {
              clearInterval(interval);

              // Perform the AJAX request after the progress bar completes
              $.ajax({
                  url: "/",
                  type: "POST",
                  data: formData,
                  contentType: false,
                  processData: false,
                  success: function (response) {
                      if (response.success) {
                          toastr.success("Files uploaded successfully.");
                          $(".right").show();
                          $("#fullName").val(response.student_data.Full_Name);
                          $("#address").val(response.student_data.City);
                          $("#dob").val(response.student_data.Date_of_Birth);
                          $("#previousSchool").val(response.student_data.School_Name);
                          $("#examYear").val(response.student_data.Exam_Year);
                          $("#symbolNo").val(response.student_data.Symbol_No);
                          $("#yearOfCompletion").val(response.student_data.Date_of_Issue);
                          $("#gpa").val(response.student_data.GPA);
                          $("#nepali").val(response.student_data.Nepali);
                          $("#english").val(response.student_data.English);
                          $("#maths").val(response.student_data.Maths);
                          $("#science").val(response.student_data.Science);
                          $("#social").val(response.student_data.Social);
                          $("#optI").val(response.student_data.Opt_I_Mathematics);
                          $("#optII").val(response.student_data.Opt_II_Science);
                      } else {
                          toastr.error(response.message);
                      }
                  },
                  error: function (xhr, status, error) {
                      toastr.error("An error occurred during file upload.");
                  }
              });

          } else {
              width++;
              progressBar.style.width = width + '%';
          }
      }, 50); // Adjust the speed of the progress bar
  });

  // Handle form save
  $("#saveForm").on("submit", function (event) {
      event.preventDefault();

      var formData = $(this).serialize();

      $.ajax({
          url: "/save",
          type: "POST",
          data: formData,
          success: function (response) {
              if (response.success) {
                  toastr.success(response.message);
              } else {
                  toastr.error(response.message);
              }
          },
          error: function (xhr, status, error) {
              toastr.error("An error occurred while saving the data.");
          },
      });
  });

  // // Handle PDF download
  // $("#downloadForm").on("submit", function (event) {
  //     event.preventDefault();

  //     $.ajax({
  //         url: "/download",
  //         type: "GET",
  //         data: $(this).serialize(),
  //         success: function (response) {
  //             if (response.success) {
  //                 window.location.href = response.pdf_url;
  //             } else {
  //                 toastr.error(response.message);
  //             }
  //         },
  //         error: function (xhr, status, error) {
  //             toastr.error("An error occurred while downloading the PDF.");
  //         },
  //     });
  // });

  $("#downloadForm").on("submit", function (event) {
    event.preventDefault();

    var formData = $(this).serialize();
    console.log(formData);  // Print form data to the console for debugging

    $.ajax({
        url: "/download",
        type: "GET",
        data: formData,
        success: function (response) {
            if (response.success) {
                window.location.href = response.pdf_url;
            } else {
                toastr.error(response.message); // This is where the error message is coming from
            }
        },
        error: function (xhr, status, error) {
            toastr.success("Downloading successfully"); // Error message here
        },
    });
});


  // Check if the form was submitted successfully and show the right section
  if (sessionStorage.getItem('formSubmitted') === 'true') {
      var certificateImage = sessionStorage.getItem('certificateImage');
      var marksheetImage = sessionStorage.getItem('marksheetImage');

      if (certificateImage) {
          var certificatePreview = document.getElementById('certificatePreview');
          certificatePreview.src = certificateImage;
          certificatePreview.style.display = 'block';
      }

      if (marksheetImage) {
          var marksheetPreview = document.getElementById('marksheetPreview');
          marksheetPreview.src = marksheetImage;
          marksheetPreview.style.display = 'block';
      }

      document.querySelector('.right').style.display = 'block';
      sessionStorage.removeItem('formSubmitted'); // Clear the flag after handling
  } else {
      // Clear sessionStorage on a regular page load
      sessionStorage.removeItem('certificateImage');
      sessionStorage.removeItem('marksheetImage');
  }
});

function previewImage(input, targetId, nameId) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
          var target = document.getElementById(targetId);
          target.src = e.target.result;
          target.style.display = "block"; 

          // Display the file name
          document.getElementById(nameId).textContent = input.files[0].name;
      };
      reader.readAsDataURL(input.files[0]); 
  }
}

function resetFormFields() {
  document.getElementById('marksheetFileName').textContent = '';
  document.getElementById('marksheetPreview').style.display = 'none';
  document.getElementById('marksheetPreview').src = ''; 
}

if (document.querySelector('.validation-error')) {  
  resetFormFields();
}

