import java.util.*;

class AirLock {
    public static void main(String args[]) {
        AirLock lock = new AirLock();
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter lock password: ");
        String userInput = sc.next();

        if (lock.checkPassword(userInput)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }
    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

    public boolean checkPassword(String password) {

        byte[] passb=password.getBytes();
        byte[] key="_scavenger__hunt_".getBytes();
        if(key.length!=passb.length)
            return false;
        byte[] XOREncoded=new byte[key.length];
        for(int i=0;i< key.length;i++)
            XOREncoded[i]=(byte)(key[i]^passb[i]);
        String base64Encoded = base64Encode(XOREncoded);
        String expected = "LBAXBw1VHlQLLSw6G0EDRyI=";
        return base64Encoded.equals(expected);
    }
}