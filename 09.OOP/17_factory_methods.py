# Key Takeaways:
# - Use @classmethod for alternate constructors returning the same class.
# - Use the factory-method pattern to encapsulate logic that chooses among subclasses.

from abc import ABC, abstractmethod


class Customer(ABC):
    @abstractmethod
    def make_payment(self, price):
        pass


class RewardsMember(Customer):
    def make_payment(self, price):
        print(
            f"""Total price for rewards member is 
          ${price * .90}, which is 10% off"""
        )


class NewCustomer(Customer):
    def make_payment(self, price):
        print(f"""Total price for new customer is ${price}""")


class Checkout:
    def _get_customer(self, customer_type):
        if customer_type == "Rewards Member":
            return RewardsMember()
        elif customer_type == "New Customer":
            return NewCustomer()

    def complete_transaction(self, customer_type, price):
        customer = self._get_customer(customer_type)
        customer.make_payment(price)


# usage
checkout = Checkout()
checkout.complete_transaction("Rewards Member", 100)
checkout.complete_transaction("New Customer", 100)

############


class LLM(ABC):
    @abstractmethod
    def complete_sentence(self, prompt):
        pass


class OpenAI(LLM):
    def complete_sentence(self, prompt):
        return prompt + " ... OpenAI end of sentence."


class Anthropic(LLM):
    def complete_sentence(self, prompt):
        return prompt + " ... Anthropic end of sentence."


class ChatBot:
    def _get_llm(self, provider):
        if provider == "OpenAI":
            return OpenAI()
        elif provider == "Anthropic":
            return Anthropic()

    def chat(self, prompt, provider):
        llm = self._get_llm(provider)
        return llm.complete_sentence(prompt)


# usage
chatbot = ChatBot()
print(chatbot.chat("Hello", "OpenAI"))
print(chatbot.chat("Hello", "Anthropic"))
