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

    $('#submit').click(function(){
        var pname = $('#pname').val();
        var image = $('#type').val();
        var intro = $('#intro').val();
        if (pname) {
            $.ajax({
                url:"add",
                type:"POST",
                data:{"pname":pname,
                       "type":image,
                       "intro":intro
                    },
                success:function(a){
                    alert(a);
                }
            
            });
        }
        return false;
    });
});
