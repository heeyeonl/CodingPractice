package sort;

public class quick_sort {

    /*
        Divide and conquer algorithm
        Recursive algorithm
        Uses a pivot element to partition the array into two parts
        Elements < pivot (left), elements > pivot (right)
        Pivot will them be in its correct sorted position
        Does this in-place (does not create arrays... save memory space)

        O(nlogn) - base 2 (worst O(n^2))
        Unstable algorithm
     */

    public static void main(String[] args) {
        int[] arr = {20, 35, -15, 7, 55, 1, -22};

        quickSort(arr, 0, arr.length);

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void quickSort(int[] input, int start, int end) {
        if (end - start < 2) {
            return;
        }
        int pivotIndex = partition(input, start, end);
        quickSort(input, start, pivotIndex);
        quickSort(input, pivotIndex + 1, end);
    }

    public static int partition(int[] input, int start, int end) {
        // This is using first as the pivot
        int pivot = input[start];
        int i = start;
        int j = end;

        while (i < j) {
            // NOTE: Empty loop body
            while (i < j && input[--j] >= pivot);
            if(i < j) {
                input[i] = input[j];
            }

            // NOTE: Empty loop body
            while (i < j && input[++i] <= pivot);
            if(i < j) {
                input[j] = input[i];
            }
        }
        input[j] = pivot;
        return j;
    }
}
