<!DOCTYPE html>
<%@page import="java.io.*,java.net.*,java.util.ArrayList;" %>
<%!
	String query=null;
	int docLen;
	String name[]=null;
	String ur[]=null;
	String tel[]=null;
	String address[]=null;
	String imageUrl[]=null;
	String type[]=null;
	String description[]=null;
	String price[]=null;
	String score[]=null;
%>
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
		<%
		String temp;
		query = request.getParameter("query");
		if(query!=null){
			if(!query.equals("")){
				String q[]=query.split(" ");
				int len=q.length;
				temp=q[0];
				if(len>1){
					for(int i=1;i<len;i++){
						temp+="+"+q[i];
					}
				}
				String urlStr = "http://localhost:8888/"+temp;
				URL url = new URL(urlStr);   
				HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
				httpURLConnection.setRequestMethod("GET");     
				InputStream is = httpURLConnection.getInputStream();   
				BufferedReader br = new BufferedReader(new InputStreamReader(is));
				temp= br.readLine();
				query=null;
				if(temp!=null){
					q=temp.split(" ");
					len=q.length;
					String re=q[0];
					if(len>1){
						for(int i=1;i<len;i++){
							re+="+"+q[i];
						}
					}
					query=temp;
					out.print("<a href='Yumming.jsp?query="+re+"'>Did you mean "+temp+" ?</a>");
				}
			}
		}
		%>
		<%
			if(query==null)
				query = request.getParameter("query");
			ArrayList<String> strList = new ArrayList<String>();
			File file = new File("../webapps/VancouverYum/Document.txt");
			InputStreamReader read = null;
			BufferedReader reader = null;
        	read = new InputStreamReader(new FileInputStream(file),"ascii");
        	reader = new BufferedReader(read);
			String line;
			while((line = reader.readLine()) != null) {
				strList.add(line);
			}
        	if(read != null) {
            	read.close();
        	}
        	if(reader != null) {
            	reader.close();
        	}
			String result=null;
			if(!query.equals("") && query!=null){
				String q[]=query.split(" ");
				int len=q.length;
				result=q[0];
				if(len>1){
					for(int i=1;i<len;i++){
						result+="+"+q[i];
					}
				}
			}
			String urlStr = "http://localhost:5123/"+result;
			URL url = new URL(urlStr);   
			HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
			httpURLConnection.setRequestMethod("GET");     
			InputStream is = httpURLConnection.getInputStream();   
			BufferedReader br = new BufferedReader(new InputStreamReader(is));
			result= br.readLine();
			if(result!=null){
				String q[]=result.split(" ");
				docLen=q.length;
				name=new String[docLen];
				ur=new String[docLen];
				tel=new String[docLen];
				address=new String[docLen];
				imageUrl=new String[docLen];
				type=new String[docLen];
				description=new String[docLen];
				price=new String[docLen];
				score=new String[docLen];
				for(int i=0;i<docLen;i++){
					name[i]=strList.get(Integer.parseInt(q[i])*10+1);
					ur[i]=strList.get(Integer.parseInt(q[i])*10+2);
					tel[i]=strList.get(Integer.parseInt(q[i])*10+3);
					score[i]=strList.get(Integer.parseInt(q[i])*10+4);
					address[i]=strList.get(Integer.parseInt(q[i])*10+5);
					description[i]=strList.get(Integer.parseInt(q[i])*10+6);
					type[i]=strList.get(Integer.parseInt(q[i])*10+7);
					imageUrl[i]=strList.get(Integer.parseInt(q[i])*10+8);
					price[i]=strList.get(Integer.parseInt(q[i])*10+9);
				}
			}
		%>
	<%for(int i=0;i<docLen;i++) {%>
      <div class="jumbotron">
		<div class="irblock">
			<div class="span img">
				<a title="Kirin" href="<% out.print(ur[i]);%>">
					<img class="img-circle" style="height: 100%; width:100%;" src="<% out.print(imageUrl[i]);%>">
				</a>
			</div>
			
			<div class="span info">
			   <div class="restaurntTitle">
					<h3 class="name"><% out.print(name[i]);%></h3>
			   </div>
				<div class="details">
					<p class="type">Type: <% out.print(type[i]);%><p>
					<p class="price">Pricing: <% out.print(price[i]);%>.</p>
					<p class="address">Location: <% out.print(address[i]);%></p>
					<p class="phone">Phone: <% out.print(tel[i]);%></p>
				</div> 
				<div class="description">
					<p class="description">Description: <% out.print(description[i]);%></p>
				</div>
				<div class="linkItem">
					<a class="url" href="<% out.print(ur[i]);%>"><% out.print(ur[i]);%></a>
				</div>
			</div>
	  	</div> 
		<hr>
      </div>
	  <% } %>
	  

	  
	  
	  
	  
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
