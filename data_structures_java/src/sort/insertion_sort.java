package sort;

public class insertion_sort {

    /*
        In-place algorithm
        O(n^2) time complexity - quadratic
        Stable algorithm
        * Comparison gap is always 1.
     */
    public static void main(String[] args) {
        int[] array = { 20, 35, -15, 7, 55, 1, -22 };
        int[] result;

//        result = sort1(array);
        result = sort2(array);

        for (int i : result){
            System.out.println(i);
        }
    }

    // my initial version (wrong, gap is bigger than 1 and inefficient)
    private static int[] sort1(int[] array) {
        for (int i = 0; i < array.length; i++) {

            int temp = array[i];
            int k = i;

            for (int j = k; j >= 0; j--) {
                System.out.println("i: " + i + ", j: " + j);
                if (array[k] < array[j]) {
                    array[k] = array[j];
                    array[j] = temp;
                    k--;
                }
            }
        }
        return array;
    }

    // more correct version
    private static int[] sort2(int[] array) {
        for (int i = 1; i < array.length; i++) {

            int temp = array[i];
            System.out.println("temp : " + temp);
            int j;

            for (j = i; j > 0 && array[j - 1] > temp; j--) {
                System.out.println("i: " + i + ", j: " + j);
                array[j] = array[j - 1];
            }
            array[j] = temp;
        }
        return array;
    }
}
