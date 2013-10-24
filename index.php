<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Vancouver Yum</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="flatstrap-master/assets/css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
      @font-face {
			font-family: "Rafa";
			src: url(font/Rafa.ttf);
		}
		
	  body {
	    background-image: url(img/r25.jpg);
		background-repeat: no-repeat;
		background-position: center center;
		background-attachment: fixed;
      }
	
      /* Custom container */

      .jumbotron {
        margin: 100px 0;
		padding: 50px 0;
		height: 300px;
        text-align: center;
		overflow:hidden;
      }
	  
      .jumbotron .btn {
	    font-family: "Rafa", Verdana, Tahoma;
        font-size: 25px;
		margin-left: 39px;
		text-align: left;
		width: 120px;
        padding: 8px;
      }
	  
     .jumbotron .theTable{
	    text-align: left;
		width: 790px;
		background-color: #ffffff;
		display: none;
      }
	  
	  .jumbotron .search{ 
	     text-align: center;
	     width: 750px;
		 height: 30px;
		 margin-left: 72px;
		
	  }
	  
	  .jumbotron .search .input-mysize { 
	     font-family: Verdana;
		 font-size: 23px;
		 width: 760px;
		 height: 30px;
		 vertical-align: top;
	  }
	  
	  
	  .footer{
	  padding: 200px 0;
	  }
	  
	  .onselect{
	    font-family: Verdana;
		font-size: 20px;
		background-color: #3498db;
		
	  }
	  
    </style>
 
  </head>

  <body>

    <div class="container">
	  
	  <div class="jumbotron">
		<img src="img/icon.png"/>
		<form class="search" action="Yumming.jsp">
			<input name="query" type="text" class="search-query input-mysize" placeholder="">
			  <table class="theTable">
              </table>
			<br><br>
			<input class="btn btn-success" type="submit" value="Yum Now!"/>
		</form>
        
      </div>


      <div class="footer">
        <p>&copy; Torres&Silvery 2013</p>
      </div>

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="flatstrap-master/assets/js/jquery.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-transition.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-alert.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-modal.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-dropdown.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-scrollspy.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-tab.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-tooltip.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-popover.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-button.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-collapse.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-carousel.js"></script>
    <script src="flatstrap-master/assets/js/bootstrap-typeahead.js"></script>
	<script type="text/javascript" src="flatstrap-master/assets/jquery-1.9.0.min.js"></script>
	
	<script type="text/javascript">
		function request(text){
			$.ajax({
				url: "/TempApps/json.jsp?query="+text,
				success: function(data) {
					d=[]
					if(typeof(data.w0)==="undefined"){
						cnt=0;
					}
					else if(typeof(data.w1)==="undefined"){
						d[0]=data.w0;
						cnt=1;
					}
					else if(typeof(data.w2)==="undefined"){
						d[0]=data.w0;
						d[1]=data.w1;
						cnt=2;
					}
					else if(typeof(data.w3)==="undefined"){
						d[0]=data.w0;
						d[1]=data.w1;
						d[2]=data.w2;
						cnt=3;
					}
					else if(typeof(data.w4)==="undefined"){
						d[0]=data.w0;
						d[1]=data.w1;
						d[2]=data.w2;
						d[3]=data.w3;
						cnt=4;
					}
					else{
						d[0]=data.w0;
						d[1]=data.w1;
						d[2]=data.w2;
						d[3]=data.w3;
						d[4]=data.w4;
						cnt=5;
					}
					$("table").html("");
					for(i=1;i<=cnt;i++){
						$("table").append("<tr><td>"+d[i-1]+"</td></tr>");
					}
					$("table tr").click(function(e){
						$("form input").val($(this).children("td").text());
						$("table").hide();
						$("form").submit();
						e.stopPropagation();
					});
					$("table tr").hover(function(){
						$(this).addClass("onselect");
					},function(){
						$(this).removeClass("onselect");
					});
				}
			});
		}
		$(document).ready(function(){
			$("form input").keyup(function(){
				_this=$(this)
				text=_this.val()
				if(text==""){
					$("table").hide();
				}
				else{
					request(text);
					$("table").show();
				}
			});
			$(document).click(function(){
				$("table").hide();
			});
		});
	</script>

  </body>
