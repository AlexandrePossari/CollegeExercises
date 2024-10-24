/// <reference = cypress>

describe("6 testes do relatório", () => {
    it("Teste de login de customer com sucesso", () => {
        cy.visit('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        cy.get('.borderM > :nth-child(1) > .btn').click()
        cy.get('#userSelect').select("Hermoine Granger")
        cy.get('form.ng-valid > .btn').click()
        cy.get('.fontBig').should("contain.text", "Hermoine Granger")
    }) 

    it("Teste de login de bank manager", () => {
        cy.visit('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        cy.get(':nth-child(3) > .btn').click()
        cy.get('[ng-class="btnClass1"]').click()
    })    

    it("Teste de deleção de customer", () => {
        cy.visit('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        cy.get(':nth-child(3) > .btn').click()
        cy.get('[ng-class="btnClass3"]').click()
        cy.get(':nth-child(1) > :nth-child(5) > button').click()

        cy.get('.home').click()
        cy.get('.borderM > :nth-child(1) > .btn').click()
        cy.get('#userSelect option').each(($ele) => {
            expect($ele).to.not.have.text('Hermione Granger')
          })
    }) 

    it("Teste de criação de customer", () => {
        cy.visit('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        cy.get(':nth-child(3) > .btn').click()
        cy.get('[ng-class="btnClass1"]').click()
        cy.get(':nth-child(1) > .form-control').type('zé first name')
        cy.get(':nth-child(2) > .form-control').type('zé last name')
        cy.get(':nth-child(3) > .form-control').type('2345')
        cy.get('form.ng-dirty > .btn').click()

        cy.get('.home').click()
        cy.get('.borderM > :nth-child(1) > .btn').click()
        cy.get('#userSelect').select("zé first name zé last name")
        cy.get('form.ng-valid > .btn').click()
        cy.get('.fontBig').should("contain.text", "zé first name zé last name")
    })      
    
    it("Teste de deposito de customer", () => {
        cy.visit('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        cy.get('.borderM > :nth-child(1) > .btn').click()
        cy.get('#userSelect').select("Hermoine Granger")
        cy.get('form.ng-valid > .btn').click()

        cy.get('[ng-class="btnClass2"]').click()        
        cy.get('.form-control').type('1000')
        cy.get('strong.ng-binding').eq(1).invoke('text').then((balanceText) => {
            let balance1 = balanceText.trim();   
            cy.get('form.ng-dirty > .btn').click()  
            cy.get('.error').should("contain.text", "Deposit Successful")
            cy.then(() => {
                cy.get('strong.ng-binding').eq(1).invoke('text').then((balance2) => {
                    expect(balance1).to.not.equal(balance2);
                })
            })
        });        
    })

    it("Teste de deposito de customer", () => {
        cy.visit('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        cy.get('.borderM > :nth-child(1) > .btn').click()
        cy.get('#userSelect').select("Hermoine Granger")
        cy.get('form.ng-valid > .btn').click()

        cy.get('[ng-class="btnClass3"]').click()        
        cy.get('.form-control').type('1000')
        cy.get('strong.ng-binding').eq(1).invoke('text').then((balanceText) => {
            let balance1 = balanceText.trim();   
            cy.get('form.ng-dirty > .btn').click()  
            cy.get('.error').should("contain.text", "Transaction successful")
            cy.then(() => {
                cy.get('strong.ng-binding').eq(1).invoke('text').then((balance2) => {
                    expect(balance1).to.not.equal(balance2);
                })
            })
        });        
    })
})
