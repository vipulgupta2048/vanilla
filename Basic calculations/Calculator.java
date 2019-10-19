import java.io.*;
public class Calculator
{
    public static void main(String args[]) throws Exception
    {
        int a=0,b=0;
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter First Number: ");
        a=Integer.parseInt(br.readLine());
        System.out.print("Enter Second Number: ");
        b=Integer.parseInt(br.readLine());
        System.out.print("Menu: \n 1-Sum\n 2-Difference\n 3-Multiplication\n 4-Division\n Enter your choice: ");
        int ch=Integer.parseInt(br.readLine());
        switch(ch)
        {
            case 1:
                System.out.println("The Sum is "+(a+b));
                break;
            case 2:
                System.out.println("The Difference is "+(a-b));
                break;
            case 3:
                System.out.println("The Product is "+(a*b));
                break;
            case 4:
                if(b==0)
                {
                    System.out.println("Division by zero");
                    System.exit(0);
                }
                System.out.println("The result of Division is "+(a/b));
                break;
            default:
                System.out.println("Wrong Choice!!");
                
        }
        
    }
}