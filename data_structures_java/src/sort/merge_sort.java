package sort;

public class merge_sort {
    /*
        Divide and conquer algorithm
        Recursive algorithm
        2 Phases: Splitting and Merging
            Splitting phase leads to faster sorting during the Merging phase
            Splitting is logical - don't create new arrays

        Splitting Phase
            - start with an unsorted array
            - Divide the array into two arrays, which are unsorted.
                The first array is the left array, and the second array is the right array.
            - Split the left and the right arrays into two arrays each
            - Keep splitting until all the arrays have only one element each
                -> these arrays are sorted
        Merging Phase
            - Merge every left/right pair of sibling arrays into a sorted array
            - After the first merge, we'll have a bunch of 2-element sorted arrays
            - Then merge those sorted arrays (left/right siblings) to end up with a bunch of 4-element sorted array
            - not in-place, uses temporary arrays

        Merging process
            - we merge sibling left and right arrays
            - We create a temporary array large enough to hold all the elements in the arrays we're merging
            - We set i to the first index of the left array, and j to the first index of the right array
     */
    public static void main(String[] args) {
        int[] array = {20, 35, -15, 7, 55, 1, -22};


        for (int i: array) {
            System.out.println(i);
        }
    }

    public static void mergeSort(int[] input, int start, int end) {
        // recursion needs breaking condition
        if (end - start < 2) { // only has one element
            return;
        }
        int mid = (start + end) / 2;
        mergeSort(input, start, mid); // {20, 35, -15} Left
        mergeSort(input, mid, end); // {7, 55, 1, -22} Right
        merge(input, start, mid, end);
    }

    public static void merge(int[] input, int start, int mid, int end) {
        // with 2 sorted arrays, if the smallest element in the right is bigger than the largest element of left
        if (input[mid - 1] <= input[mid]) { // optimization
            return;
        }

    }
}
