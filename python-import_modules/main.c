#include <stdio.h>
#include <string.h>

// Function to generate combinations of characters
void brute_force_password(const char* password) {
    const char characters[] = "abcdefghijklmnopqrstuvwxyz0123456789";  // Character set
    int max_length = 8;  // Maximum length of the password
    int n = strlen(characters);
    char guess[9] = {0};  // Buffer to hold the guessed password

    // Iterate through increasing lengths of guesses
    for (int length = 1; length <= max_length; length++) {
        int indices[length];  // To hold the indices of characters
        memset(indices, 0, sizeof(indices));  // Initialize to zero

        while (1) {
            // Form the current guess
            for (int i = 0; i < length; i++) {
                guess[i] = characters[indices[i]];
            }
            guess[length] = '\0';  // Null-terminate the string

            printf("Trying: %s\n", guess);

            // Check if the guess matches the password
            if (strcmp(guess, password) == 0) {
                printf("Password guessed successfully: %s\n", guess);
                return;
            }

            // Increment the indices array
            int i;
            for (i = length - 1; i >= 0; i--) {
                if (indices[i] < n - 1) {
                    indices[i]++;
                    break;
                } else {
                    indices[i] = 0;
                }
            }

            // Break the loop if all combinations are tried
            if (i < 0) {
                break;
            }
        }
    }

    printf("Failed to guess the password.\n");
}

int main() {
    char password[9];  // Buffer to hold the input password
    printf("Enter a password for the program to guess (max 8 characters): ");
    scanf("%8s", password);  // Read up to 8 characters from user input

    brute_force_password(password);  // Call the brute-force function

    return 0;
}