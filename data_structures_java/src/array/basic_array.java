package array;

public class basic_array {

     /*
         Array

         - Contiguous block in memory.
         - When you create an array, size needs to be set.
                 and size cannot be resized. (static length, not dynamic structure)
         - Every element occupies the same amount of space in memory.
                ex) int = 4 bytes, length 7 * 4bytes = 28byte size of array.
         - If an array starts at memory address x,
                and the size of each element in the array is y,
                we can calculate the memory address of the ith element by using: (x + i * y)
         - To access elements, you need to have index of the array.
         - Big(O) = for the array, in worst case it will take O(n) if we don't know the index of the val.
     */
    public static void main(String[] args) {
        int[] intArray = new int[7]; // size needs to be set

        for(int i = 0; i < intArray.length; i++) {
            intArray[i] = i;
            System.out.println("at["+ i + "]: " + intArray[i]);
        }
    }
}