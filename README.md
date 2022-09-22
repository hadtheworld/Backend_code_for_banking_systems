# Backend_code_for_banking_systems
This is a backend code using python where instructions are read from the file passed line by line and are executed to give the output for BALANCE command. It uses calls like LOAN, PAYMENT,BALANCE to apply different functionalities.these commands(calls) are passes at beginning of every line of the file, such as  "LOAN IDIDI Dale 5000 1 6", "PAYMENT IDIDI Dale 1000 5", "BALANCE IDIDI Dale 3".

#**Detailed Description:-**

The program should take as input:

1. The bank name, borrower name, principal, interest and term.
2. Lump sum payments if any.
3. Given the bank name, borrower name, and EMI number, the program should print the total amount paid by the user (including the EMI number mentioned) and the remaining number of EMIs.

The output is:- 
1. Amount paid so far, and number of EMIs remaining for the user with the bank (It will be shown in BALANCE Command only)

Input Commands
There are 3 input commands defined to separate out the actions. The input format starts with either of these commands i.e LOAN, PAYMENT, BALANCE


LOAN
The LOAN command receives a Bank_name, Borrower_name, Principal_Amount, No_of_Years of Loan period and the Rate_of_Interest(ROI) along with it.
Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST
Example- LOAN IDIDI Dale 10000 5 4 means a loan amount of 10000 is paid to Dale by IDIDI for a tenure of 5 years at 4% rate of interest.

PAYMENT
The PAYMENT command receives a Bank_name, Borrower_name, Lump_sum amount and EMI_number along with it. The EMI number indicates that the lump sum payment is done after that EMI.
Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO
Example - PAYMENT MBI Dale 1000 5 means a lump sum payment of 1000 was done by Dale to MBI after 5 EMI payments.

BALANCE
The BALANCE command receives a Bank_name, Borrower_name and a EMI_number along with it. It prints the total amount paid by the borrower, including all the Lump Sum amounts paid including that EMI_number, and the no of EMIs remaining.
Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
Example - BALANCE MBI Harry 12 means - print the amount paid including 12th EMI, and EMIs remaining for user Harry against the lender MBI.
Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT

Assumptions
1. Repayments will be paid every month as EMIs until the total amount is recovered.
2. Lump sum amounts can be paid at any point of time before the end of tenure.
3. The EMI amount will be always ceiled to the nearest integer. For example 86.676767 can be ceiled to 87 and 100.10 to 101.
4. The no of EMIs should be ceiled to the nearest whole number. For example 23.79 will be ceiled to 24 and 23.1 will also be ceiled to 24.
5. If the last EMI is more than the remaining amount to pay, then it should be adjusted to match the amount remaining to pay. E.g. if the remaining amount to pay is 150 and your EMI is 160, then the last EMI amount paid should be 150.
6. The total amount remaining at any EMI number should always include the EMIs paid and lump sum payments until that number. For example if there was a lump sum payment after EMI number 10, then the balance command for EMI number 10 should include the lump sum payment as well.
