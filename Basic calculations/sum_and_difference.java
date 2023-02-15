import java.io.*;
public class sum_and_difference
{
    public static void main(String args[]) throws Exception
    {
        int a=0,b=0;
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the First Number: ");
        a=Integer.parseInt(br.readLine());
        System.out.println("Enter the Second Number: ");
        b=Integer.parseInt(br.readLine());
        System.out.println("The Sum is: "+(a+b));
        System.out.println("The Difference is: "+(a-b));
    }
}