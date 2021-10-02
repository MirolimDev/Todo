$(document).ready(function(s){

    $(document).on('click', '.delete_task',function(s){
        s.preventDefault()

        let id = $(this).attr('id')
        alert(id + '  salom ')  
  
        $.ajax({

            url: "http://localhost:8000/delete/",
            type: "POST",
            data: {
                product_id: id,
            },
            success: function(html){
                $('.todo-list').html(html)
            },
            error: function(html){
                alert('error')
            }
        })
    })

})