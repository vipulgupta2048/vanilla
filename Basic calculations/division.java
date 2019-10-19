import java.io.*;
public class division
{
    public static void main(String args[]) throws Exception
    {
        int a=0,b=0;
        BufferedReader d=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter numerator: ");
        a=Integer.parseInt(d.readLine());
        System.out.println("Enter denominator: ");
        b=Integer.parseInt(d.readLine());
        if(b==0)
        {
            System.out.println("Denominator cannot be 0");
            System.exit(0);
        }
        System.out.println("Result: "+(a/b));
    }
}