alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


encode_or_decode = input("Would you like to encode or decode a message?:\n").lower()
secret_message = input("Type the message:\n").lower()
key = int(input("Type the key:\n"))


def encode(secret_message, key):
    output_message = ""

    for i, letter in enumerate(secret_message):
        for j, let in enumerate(alphabet):
            if alphabet[j] == secret_message[i]:
                new_pos = j + key
                if new_pos >= 26:
                    new_pos = new_pos % 26
                    output_message = secret_message.replace(
                        secret_message[i], alphabet[new_pos]
                    )
                else:
                    output_message += alphabet[new_pos]
    return output_message


def decode(secret_message, key):
    key *= -1
    output_message = ""

    for i, letter in enumerate(secret_message):
        for j, let in enumerate(alphabet):
            if alphabet[j] == secret_message[i]:
                new_pos = j + key
                if new_pos >= 26:
                    new_pos = new_pos % 26
                    output_message = secret_message.replace(
                        secret_message[i], alphabet[new_pos]
                    )
                else:
                    output_message += alphabet[new_pos]
    return output_message


# rome
# 7
if encode_or_decode == "encode":
    print(encode(secret_message, key))
elif encode_or_decode == "decode":
    print(decode(secret_message, key))
else:
    raise ValueError("Please pick a operation")
