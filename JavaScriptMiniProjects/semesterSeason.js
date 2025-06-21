function semesterIs(month) {

    const months = {

    'January': 0,
    'February': 1,
    'March': 2,
    'April': 3,
    'May': 4,
    'June': 5,
    'July': 6,
    'August': 7,
    'September': 8,
    'October': 9,
    'November': 10,
    'December': 11
    
}
    // console.log(month);
    
    // console.log(months.month)

    // console.log(months[month])

    // console.log(Object.values(months))
    
    if((months[month] >= months.January) && (months[month] <= months.May)) return 'Spring';
        
    else if ((months[month] > months.May) && (months[month] <= months.July)) return 'Summer';

    else return 'Fall';   
}