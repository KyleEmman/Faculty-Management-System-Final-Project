function report(fileName) {
    const doc = new jsPDF()
    const headers = document.getElementById('temp-table')
    doc.fromHTML(headers, 15, 5)
    doc.autoTable({
        startY: 25,
        pageBreak: 'auto',
        html: '#main-table',
    })
    doc.save(fileName)
}
