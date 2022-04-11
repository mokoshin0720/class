class Account
    attr_accessor :bank_money
    def initialize
        @bank_money = 0
    end

    def deposit(n)
        @bank_money += n
    end

    def withdraw(n)
        if is_withdraw(n) == false
            return
        end
        @bank_money -= n
    end

    def transfer(x, n)
        if is_withdraw(n) == false
            return
        end
        @bank_money -= n
        x.bank_money += n
    end

    def balance
        @bank_money
    end

    def is_withdraw(n)
        if @bank_money < n
            puts "you don't have enough money"
            return false
        end
        return true
    end
end
