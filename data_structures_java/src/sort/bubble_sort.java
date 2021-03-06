package sort;


/*
    In-place algorithm
    O(n^2) time complexity - quadratic algorithm
        It will take 100 steps to sort 10 items.
    Algorithm degrades quickly.
    Not really efficient so not used a lot.
 */
public class bubble_sort {

    public static void main(String[] args) {
        int[] bubble = {20, 35, -15, 7, 55, 1, -22};
        int numSwap = 0;
        for(int i=bubble.length-1; i > 0; i--) {    // from the last to the first index
            for (int j=0; j < i; j++) {
                if(bubble[j] > bubble[j+1]) {
                    swap(bubble, j, j + 1);         // ascending order
                    numSwap++;
                }
            }
        }

        for (int i: bubble) {
            System.out.print(i + " ");
        }
        System.out.println("\nnumber of swaps: " + numSwap);
    }

    private static void swap(int[] array, int i, int j) {
        if (i == j) {
            return;
        }
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
