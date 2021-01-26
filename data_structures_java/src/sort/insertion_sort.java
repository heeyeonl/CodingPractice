package sort;

public class insertion_sort {

    /*
        In-place algorithm
        O(n^2) time complexity - quadratic
        Stable algorithm
     */
    public static void main(String[] args) {

        int[] array = { 20, 35, -15, 7, 55, 1, -22 };

        for (int i = 0; i < array.length; i++) {
            int temp = array[i];
            int k = i;

            for (int j = k; j >= 0; j--) {
                if (array[k] < array[j]) {
                    array[k] = array[j];
                    array[j] = temp;
                    k--;
                }
            }
//            Another way to do this shifting... (int i = 1)
//            int j;
//            for (j = i; j > 0 && array[j - 1] > temp; j--) {
//                array[j] = array[j - 1];
//            }
//            array[j] = temp;
        }

        for (int i : array){
            System.out.println(i);
        }
    }
}
