package Integers;

import java.util.ArrayList;
import java.util.List;

public class FizzBuzz_412 {

    public static void main(String[] args) {
        int n = 15;
        List<String> result = fizzBuzz(n);
        System.out.println(result);
    }

    public static List<String> fizzBuzz(int n) {
        int i = 1;
        List<String> result = new ArrayList<>();
        while(i <= n) {
            if (i % 3 == 0 && i % 5 == 0) {
                result.add("FizzBuzz");
            }
            else if (i % 3 == 0) {
                result.add("Fizz");
            }
            else if (i % 5 == 0) {
                result.add("Buzz");
            }
            else {
                result.add(Integer.toString(i));
            }
            i++;
        }
        return result;
    }
}
