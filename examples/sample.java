public class BankService {

    public void processTransaction(String accountNo, double amount) {

        System.out.println("Transaction started");

        try {
            // Validation
            if (accountNo == null || accountNo.isEmpty()) {
                System.out.println("Invalid account number");
                return;
            }

            // Check transaction amount
            if (amount <= 0) {
                System.out.println("Invalid amount");
            } else {

                // High value transaction check
                if (amount > 10000) {
                    System.out.println("High value transaction detected");
                } else {
                    System.out.println("Normal transaction");
                }

                // Simulate processing steps
                for (int i = 1; i <= 3; i++) {
                    System.out.println("Processing step " + i);
                }

                System.out.println("Transaction successful");
            }

        } catch (Exception e) {

            System.out.println("Transaction failed due to system error");

        } finally {

            System.out.println("Transaction process completed");
        }

        System.out.println("End of method");
    }
}
