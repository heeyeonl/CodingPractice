package sort;

public class shell_sort {
    /*
        Variation of insertion sort
        Insertion sort chooses which element to insert using a gap of 1.
        Shell sort starts out using a larger gap value.
        The gap is reduced. (The last gap value is always 1)

        In-place algorithm.
        Difficult to know Big(O), but worst case O(n^2) but it can perform much better.
        Doesn't require as much shifting as insertion sort.
        Unstable algorithm.
     */
    public static void main(String[] args) {
       int[] intArray = { 20, 35, -15, 7, 55, 1, -22 };

       // loops for gap, outer index to move up, and inner index to compare
        for (int gap = intArray.length / 2; gap > 0; gap /= 2) {

            for(int i = gap; i < intArray.length; i++) {
                int j = i;
                int newElement = intArray[i];

                while (j >= gap && intArray[j - gap] > newElement) { // use newElement instead of intArray[i] because it keeps changing
                    intArray[i] = intArray[j - gap];
                    j -= gap;
                }
                intArray[j] = newElement;
            }
        }


        for (int i: intArray) {
            System.out.println(i);
        }
    }
}
