%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<html lang="en" dir="ltr">
   <head>
      <meta charset="utf-8">
      <title>Todo</title>
      <link rel="stylesheet" href="static/main.css">
      <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
   </head>

   <style>


   .container {
      justify-content: center;
      text-align: center;
      width: auto;
      margin: auto;
  }

   </style>


      <div class="btn">
         <span class="fas fa-bars"></span>
      </div>
      <nav class="sidebar">
          <div class="text">
              Menu
          </div>
          <ul>
              <li class="active"><a href="/">Home</a></li>
              <li>
                <a href="/new" class="feat-btn">Add Task
                </a>
                
              </li>
              <li>
                <a href="/todo" class="serv-btn">View List
              </li>
              <li><a href="/find_item">Edit List</a></li>
          </ul>
        </nav>

      <div class = "content">
       <h1>All items are as follows:</h1>
        <div style="display:flex;justify-content:center;align-items:center;">
          <table border="5">
          %for row in rows:
            <tr>
            %for col in row:
              <td>{{col}}</td>
            %end
            </tr>
          %end
          </table>
          <br>
        </div>


        %# edit item number returned to /find_item POST method function
        <form action = "/find_item" method="POST" >                     
            <label for="no">What numbered item would you like to edit?>
            <input name="todoID" type ="number">
            <input type="submit" name = "save"value = "Query">
        </form>


        <form action = "/" >
            <button type="submit"> Homepage</button>
        </form>
      </div>

    


      <script>
         $('.btn').click(function(){
           $(this).toggleClass("click");
           $('.sidebar').toggleClass("show");
         });
           $('.feat-btn').click(function(){
             $('nav ul .feat-show').toggleClass("show");
             $('nav ul .first').toggleClass("rotate");
           });
           $('.serv-btn').click(function(){
             $('nav ul .serv-show').toggleClass("show1");
             $('nav ul .second').toggleClass("rotate");
           });
           $('nav ul li').click(function(){
             $(this).addClass("active").siblings().removeClass("active");
           });
      </script> 


  
</html>
      


