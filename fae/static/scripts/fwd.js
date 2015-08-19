$(document).ready(function(){
	
	$(".submit-file-btn").click(function(){
	    var fd = new FormData();
        fd.append("file",1);
        fd.append("file",$("#path").get(0).files[0]);
        alert("hell wrod");
        $.ajax({
            url: "upload",
            type: "POST",
            processData: false,
            contentType: false,
            data:fd,
            success:function(d) {
                window.file_path = d;
                alert(d);
           }
        });
        return false;
	});
});
