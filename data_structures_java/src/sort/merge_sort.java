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
     */
}
