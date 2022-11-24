function deafGrandma() {
    let bye = 0
    let text = prompt('HEY KID!')
    while (bye < 2) {
        if (text.toLowerCase() === 'goodbye!' && bye === 1) {
            text = alert('LATER, SKATER!')
            break
        } else if (text.toLowerCase() === 'goodbye!') {
            bye++ 
            text = prompt('LEAVING SO SOON?')
        } else if (text === "") {
            text = prompt('WHAT?!')
        } else if (text === text.toLowerCase()) {
            text = prompt('SPEAK UP, KID!')
        } else if (text === text.toUpperCase()) {
            text = prompt('NO, NOT SINCE 1946!')
        }  
    }
}
deafGrandma()