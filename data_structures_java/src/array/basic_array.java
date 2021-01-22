package array;

public class basic_array {

    // Array
    // Contiguous block in memory.
    // When you create an array, size needs to be set. (static length)
    // Size cannot be resized.
    // Every element occupies the same amount of space in memory.
    //      ex) int = 4 bytes, length 7 * 4bytes = 28byte size of array.
    // To access elements, you need to have index of the array.
    public static void main(String[] args) {
        int[] intArray = new int[7]; // size needs to be set

        for(int i = 0; i < intArray.length; i++) {
            intArray[i] = i;
            System.out.println("at["+ i + "]: " + intArray[i]);
        }
    }
}