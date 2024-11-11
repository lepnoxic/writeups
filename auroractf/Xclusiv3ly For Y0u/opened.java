import java.util.*;import java.util.*;

class not_taken {
    public static void main(String args[]) {
        not_taken ob = new not_taken();
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the flag");
        String input = in.next();
        if (ob.match(input)) {
            System.out.println("Correct Flag entered!");
        } else {
            System.out.println("Incorrect Flag entered! Try Again");
        }
    }

    public String hexencode(byte[] input) {
        StringBuilder result = new StringBuilder();
        for (byte b : input) {
            result.append(String.format("%02X", b));
        }
        return result.toString();
    }

    boolean match(String password) {
        byte[] pws = password.getBytes();
        byte[] key = "w3__ar3_mi5t_is_key".getBytes();

        if (key.length != pws.length)
            return false;

        byte[] Xored = new byte[key.length];
        for (int i = 0; i < key.length; i++)
            Xored[i] = (byte) (key[i] ^ pws[i]);

        String hexencoded = hexencode(Xored);
        System.out.println(hexencoded);

        String expectedHex = "16502B07091C6F183615442A0717005A1104";

        return hexencoded.equals(expectedHex);
   }
}