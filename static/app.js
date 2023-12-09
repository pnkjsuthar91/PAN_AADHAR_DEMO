$(document).on("click", ".browse", function() {
  var file = $(this).parents().find(".file");
  file.trigger("click");
});
$('input[type="file"]').change(function(e) {
  var fileName = e.target.files[0].name;
  $("#file").val(fileName);

  var reader = new FileReader();
  reader.onload = function(e) {
    // get loaded data and render thumbnail.
    document.getElementById("preview").src = e.target.result;
  };
  // read the image file as a data URL.
  reader.readAsDataURL(this.files[0]);
});

$("#post-btn").click(function(){
    var formData = new FormData();
    formData.append('file', $('#document')[0].files[0]);
    var ajaxTime= new Date().getTime();
//    e.preventDefault();
  $.ajax({
        url: "/extract/info/",
       type: "POST",
       data:  formData,
       contentType: false,
             cache: false,
       processData:false,
       success: function(response){
            console.log(response)
//            response = $.parseJSON(data);
            $.each(response, function(field, value) {
                var $tr = $('<tr>').append(
                    $('<td>').text('1'),
                    $('<td>').text(field),
                    $('<td>').text(value)
                ).appendTo('#document-table');
            });
            var totalTime = new Date().getTime()-ajaxTime;
            console.log(totalTime)

       },
        error: function(e) {
            console.log(e)
            alert("!Oops something went wrong.")
        }
    });
});

