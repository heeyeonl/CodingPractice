package sort;

/*
    In-place algorithm (no extra memory used)
    O(n^2) time complexity - quadratic
    Doesn't require as much swapping as bubble sort
    Unstable algorithm

    Steps
        Traverse from the beginning
        Compare first two and set i to largest element
        Keep going until the end
        Change last element to the biggest element of the array
        Repeat
 */
public class selection_sort {

    public static void main(String[] args) {
        int[] selection = { 20, 35, -15, 7, 55, 1, -22 };

        for (int i = selection.length - 1; i > 0; i--) {
            int largest = 0; // so far we know the first element is largest. (index 0)

            for (int j = 1; j <= i; j++ ) { // start at index 1, largest is index 0
                if (selection[j] > selection[largest]) {
                    largest = j;
                }
            }
            swap(selection, i, largest);
        }


        for (int i: selection) {
            System.out.println(i);
        }

    }

    public static void swap(int[] array, int i, int j) {
        if (i == j) {
            return;
        }

        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
