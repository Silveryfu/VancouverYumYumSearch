<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Yumming!</title>
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
		background-color: #ffffff;
      }

	  .navbar .navbar-inner {
	    text-align:center;
		vertical-align: middle;
		padding-top: 20px;
		background-color: #5EAB99;
	  }
	  
	  .navbar .navbar-inner .form-search .input-medium{
		width: 500px;
		height: 20px;
		margin: 0px;	
		margin-left: 0px;

	  }
	  
	  .navbar .navbar-inner .form-search .btn{
		font-family: "Rafa", Verdana, Tahoma;
		font-size: 20px;
		height: 20px;
		width: 50px;
		margin: 0px;	

	  }
	  
	  .container-narrow {
	    /*background-color: #2980b9;*/
        margin: 100px auto;
        max-width: 700px;
      }
	  
      .container-narrow > hr {
	    border-top: 0px;
		padding-top: 900px;
        margin-top: 30px 0;
      }
	  
	  .jumbotron {
	    /*background-color: #8e44ad;*/
        margin: 10px 0;
		padding: 10px 0;
        text-align: center;
		overflow:hidden;
      }
	  
	  .jumbotron .irblock { 
		 /*background-color: #2ecc71;*/
	     width: 700px;
		 height: 250px;
		 overflow:hidden;
	  }
	  
	  .jumbotron .irblock .img { 
		 /*background-color: #e67e22;*/
	     width: 200px;
		 height: 250px;
		 overflow:hidden;
	  }
	  
	  .jumbotron .irblock .info { 
		 /*background-color: #f1c40f;*/
		 text-align: left;
		 line-height:15px;
		 width: 450px;
		 height: 250px;
		 overflow:hidden;
	  } 
	  
	  .jumbotron .irblock .info .details{ 
		 /*background-color: #f1c40f;*/
		 width: 450px;
		 height: 120px;
		 line-height:16px;
		 font-family: serif;
		 font-style: italic;
		 font-size:15px;
		 padding-top: 5px;
		 overflow:hidden;
	  } 
	  
	  .jumbotron .irblock .info .description{ 
		 /*background-color: #f1c40f;*/
		 width: 450px;
		 height: 40px;
		 line-height:17px;
		 font-family: serif;
		 font-size:16px;
		 padding-top: 5px;
		 overflow:hidden
	  } 
	  
	  .jumbotron .irblock .info .name{ 
		 color: #e74c3c;
		 margin-top:0px; 
		 font-size:45px;
	  } 
	  
	  .jumbotron .irblock .info .linkItem{ 
		 color: #3498db;
		 font-size:15px;
	  } 
	  

	  .footer{
	  padding-top: 5px 0;
	  }

      /* Main marketing message and sign up button */
    </style>


  </head>
  <body>
  
	<div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
         <form class="form-search" action="#">
			<input type="text" class="input-medium search-query" name="query"/>
			<a class="btn btn-success" onclick="$('form').submit();">Yum!</a>
		</form>
	 </div>
    </div>
  

  
    <div class="container-narrow">
		<?php
		$query = $_GET["query"];
		if($query != NULL){
			if(strcmp($query, "") != 0){
				$q = preg_split("/[\s]+/", $query);
				$temp = join("+", $q);
				$temp = file_get_contents("http://localhost:8888/" . $temp);
				if($temp != NULL && strcmp($temp, "") != 0){
					$q = preg_split("/[\s]+/", $temp);
					$temp = join("+", $q);
					$query = $temp;
					print("<a href='Yumming.php?query=" . $temp . "'>Did you mean " . join(" ", $q) . " ?</a>");
				}
			}
		}
		?>
		<?php
			if($query == NULL)
				$query = $_GET["query"];
			$strList = file_get_contents("https://raw.githubusercontent.com/Silveryfu/Yumcouver.com/8b260c4d673bc16e744de94a53c99853c0850a83/Docs/Document.txt");
			$strList = explode("\n", $strList);
			if(! strcmp($query, "") && $query != NULL){
				$q = preg_split("/[\s]+/", $query);
				$result = join("+", $q);
			}
			$result = file_get_contents("http://localhost:5123/" . $result);
			if($result != NULL){
				$q = preg_split("/[\s]+/", $result);
				$docLen = count($q);
				$name = array();
				$ur = array();
				$tel =  array();
				$address = array();
				$imageUrl = array();
				$type = array();
				$description = array();
				$price = array();
				$score = array();
				for($i = 0; $i < $docLen; $i++){
					$name[] = $strList[intval($q[$i])*10+1];
					$ur[] = $strList[intval($q[$i])*10+2];
					$tel[] = $strList[intval($q[$i])*10+3];
					$score[] = $strList[intval($q[$i])*10+4];
					$address[] = $strList[intval($q[$i])*10+5];
					$description[] = $strList[intval($q[$i])*10+6];
					$type[] = $strList[intval($q[$i])*10+7];
					$imageUrl[] = $strList[intval($q[$i])*10+8];
					$price[] = $strList[intval($q[$i])*10+9];
				}
			}
		?>
	<?php
	for($i=0; $i < $docLen; $i++) {
	?>
      <div class="jumbotron">
		<div class="irblock">
			<div class="span img">
				<a title="Kirin" href="<?php print($ur[$i]);?>">
					<img class="img-circle" style="height: 100%; width:100%;" src="<?php print($imageUrl[$i]);?>">
				</a>
			</div>
			
			<div class="span info">
			   <div class="restaurntTitle">
					<h3 class="name"><?php print($name[$i]); ?></h3>
			   </div>
				<div class="details">
					<p class="type">Type: <?php print($type[$i]); ?><p>
					<p class="price">Pricing: <?php print($price[$i]); ?>.</p>
					<p class="address">Location: <?php print($address[$i]); ?></p>
					<p class="phone">Phone: <?php print($tel[$i]); ?></p>
				</div> 
				<div class="description">
					<p class="description">Description: <?php print($description[$i]);?></p>
				</div>
				<div class="linkItem">
					<a class="url" href="<?php print($ur[$i]);?>"><?php print($ur[$i]);?></a>
				</div>
			</div>
	  	</div> 
		<hr>
      </div>
	  <?php } ?>
	  

	  
	  
	  
	  
      <hr>


      <div class="footer">
        <p>&copy; Torres&Silvery 2013</p>
      </div>

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://code.jquery.com/jquery-1.9.0.js"></script>
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
    <script>
  	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  	})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  	ga('create', 'UA-50816132-1', 'yumcouver.com');
  	ga('send', 'pageview');

	</script>
  </body>
</html>
