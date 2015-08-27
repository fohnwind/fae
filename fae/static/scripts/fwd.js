$(document).ready(function(){
	
	$(".submit-file-btn").click(function(){
	    var fd = new FormData();
        fd.append("file",1);
        fd.append("file",$("#path").get(0).files[0]);
        $.ajax({
            url: "upload",
            type: "POST",
            processData: false,
            contentType: false,
            data:fd,
            success:function(d) {
                window.file_path = d;
                alert("sucess");
           }
        });
        return false;
	});

	$(".submit-changefile-btn").click(function(){
	    var fd = new FormData();
        fd.append("file",1);
        fd.append("file",$("#path").get(0).files[0]);
        var a = confirm("确认提交新文件?");
        if (a) {
            $.ajax({
                url: "upload",
                type: "POST",
                processData: false,
                contentType: false,
                data:fd,
                success:function(d) {
                    window.file_path = d;
                    alert("sucess");
                }
            });
        }
        return false;
    });


    $('#create-project').click(function(){
        alert("123");
        var pname = $('#pname').val();
        var image = $('#ptype').val();
        var intro = $('#intro').val();
        var fileurl = '';
        if (typeof(window.file_path)!="undefined") {
            fileurl = window.file_path
        }
  
        if (pname) {
    
            $.ajax({
                url:"add",
                type:"POST",
                data:{"pname":pname,
                       "ptype":image,
                       "intro":intro,
                       "fileurl":fileurl
                    },
                success:function(a){
                    window.location.href = a;
                }
            
            });
        }
        return false;
    });
});
