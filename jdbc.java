package jdbcdemo1;

import java.sql.*;

	public class Demo1 {

		public static void main(String[] args) {
			// TODO Auto-generated method stub

			
			try {
				
				Class.forName("com.mysql.jdbc.Driver");
				Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/manasi1","root","Password123");
				Statement stmt= con.createStatement();
				stmt.execute("insert into Emp values(101,'Ramesh','34','80000','Manager')");
				stmt.close();
				System.out.println("Data saved successfully");
				
			}
			catch(Exception e) {
				System.out.println(e);
				
			}
		}

	}


