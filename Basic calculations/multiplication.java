import java.io.*;
public class multiplication
{
    public static void main(String args[]) throws Exception
    {
        int a=0,b=0;
        BufferedReader br=new BufferedReader (new InputStreamReader(System.in));
        System.out.println("Enter the First Number: ");
        a=Integer.parseInt(br.readLine());
        System.out.println("Enter the Second Number: ");
        b=Integer.parseInt(br.readLine());
        System.out.println("The product is: "+(a*b));
    }
}