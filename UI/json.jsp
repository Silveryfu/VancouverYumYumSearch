<%@page pageEncoding="ascii" import="java.sql.*" %>
<%  response.setContentType("application/json");
	Class.forName("com.mysql.jdbc.Driver");
	String connectionUrl = "jdbc:mysql://yumcouver.cwob5qq6ng7q.us-east-1.rds.amazonaws.com:3306/yumcouver?user=read-only&password=read-only";
	Connection conn = DriverManager.getConnection(connectionUrl);
	Statement stmt = conn.createStatement();
	String words=request.getParameter("query");
	if(words!=null){
	String wordSet[] = words.split(" ");
	int i=0;
	boolean flag=true;
	ResultSet rs=null;
	for(;i<wordSet.length-1;i++){
		rs = stmt.executeQuery("SELECT word FROM yum_dictionary where word = '"+wordSet[i]+"'");
		if(!rs.next()){
			flag=false;
			break;
		}
	}
	if(flag==true){
		rs = stmt.executeQuery("SELECT word FROM yum_dictionary where word like '"+wordSet[i]+"%' order by word");
	}
	out.print("{");
	i=0;
	if(rs.next()){
		String word=rs.getString(1);
		words="";
		for(int j=0;j<wordSet.length-1;j++){
			words = words+wordSet[j]+" ";
		}
		words = words+word;
		out.print("\"w"+i+"\":\""+words+"\"");
		i++;
		while(rs.next() && i<5){
			word=rs.getString(1);
			words="";
			for(int j=0;j<wordSet.length-1;j++){
				words = words+wordSet[j]+" ";
			}
			words = words+word;
			out.print(",\"w"+i+"\":\""+words+"\"");
			i++;
		}
	}
	out.print("}");
	}
	if(conn != null) {
		conn.close();
	}
%>