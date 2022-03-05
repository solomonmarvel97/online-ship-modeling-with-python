class AccountClass:
    id: str
    email: str
    password: str
    createdat: str
    updateda: str

    def __init__(self, id: str, email: str, password: str, createdat: str, updateda: str) -> None:
        self.id = id
        self.email = email
        self.password = password
        self.createdat = createdat
        self.updateda = updateda


class Account:
    account: AccountClass

    def __init__(self, account: AccountClass) -> None:
        self.account = account
