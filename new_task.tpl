
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

   <body>
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
    </body>
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

      <div class = "container">
        %#template for the form for a new task
        <p>Add a new task to the ToDo list:</p>
        <form action="/new" method="GET">
            <input type="text" size="100" maxlength="100" name="task">
            <input type="submit" name="save" value="save">
        </form>
      <div>

</html>
