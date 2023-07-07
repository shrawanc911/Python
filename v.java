public class v{
    public static void main(String[] args) {
        int a = 5;
        righttriangle(a);
        pyramid(a);

        
    }

    static void righttriangle(int a){
        for(int i = 0 ; i<a;i++)
        {
            for (int j = 0; j < i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pyramid(int a){
        for (int i = 0; i < a; i++) {

            for (int j = 0; j < a-i; j++) {
                System.out.print(" ");
            }

            for (int k = 0; k < i; k++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }


}