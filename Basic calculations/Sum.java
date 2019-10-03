import java.io.*;
public class sum
{
    public static void main(String args[]) throws Exception
    {   
        DataInputStream d=new DataInputStream(System.in);
        int a=0,b=0;
        System.out.println("Enter the numbers-->\na:");
        a=Integer.parseInt(d.readLine());
        System.out.println("b:");
        b=Integer.parseInt(br.readLine());
	System.out.println("The sum is "+(a+b));
     }
}

