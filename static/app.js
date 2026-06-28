// Bahandisation client SPA app.js

const productOptions = [
  "Chicken Patty",
  "French Fries",
  "Onion Rings",
  "Burger Bun",
  "Tomato",
  "Cheese",
  "Rotten Vegetables",
  "Damaged Packaging",
  "Burned Food",
  "Wrong Product",
  "Missing Ingredients"
];

const employeeOptions = ["Айдана С.", "Нурбек К.", "Мария Л.", "Ержан Т.", "Команда смены"];
const reasonValues = ["Dropped", "Not cooked", "Bad quality", "Burned", "Damaged", "Expired", "Supplier defect", "Other"];
const ROLE_STORAGE_KEY = "bahandisation-role-v2";

const copy = {
  ru: {
    brand: "Bahandisation",
    topEyebrow: "Bahandisation AI",
    navEmployee: "Сотрудник",
    navReport: "Списание",
    navManager: "Менеджер",
    navAnalytics: "AI-точность",
    bottomHome: "Дом",
    bottomReport: "Заявка",
    bottomApprove: "Проверка",
    language: "Язык",
    employeeTitle: "Операционный AI-центр Bahandi",
    reportTitle: "Новая заявка",
    managerTitle: "Проверка списаний",
    analyticsTitle: "Точность Roboflow",
    authHeroTitle: "AI-центр списаний Bahandi",
    authHeroText: "Введите ваши учетные данные. Работник перейдет к быстрому сценарию фото -> AI -> причина -> отправка. Менеджер попадет в кабинет проверки, аналитики и контроля поставщиков.",
    authCreateTitle: "Войдите в систему",
    authCreateText: "Используйте ваши учетные данные для авторизации в Bahandisation.",
    authRoleLabel: "Роль",
    authEmployeeTag: "Работник",
    authEmployeeTitle: "Авторизация работника",
    authManagerTitleShort: "Админ",
    authFirstName: "Имя",
    authLastName: "Фамилия",
    authEmail: "Email / Логин",
    authEmployeeName: "Имя работника",
    authBranchName: "Торговая точка",
    authContinue: "Войти",
    authAccountHint: "Нужна помощь?",
    authSignIn: "Поддержка",
    authEmployeeButton: "Войти в систему",
    authManagerTag: "Админ",
    authManagerTitle: "Авторизация",
    authManagerName: "Имя пользователя",
    authManagerZone: "Филиал",
    authManagerButton: "Войти в систему",
    heroTitle: "Сфотографируйте списание. Bahandisation скажет, что случилось.",
    heroText: "Наш API принимает фото, отправляет его в Roboflow на сервере и сразу возвращает текст: какой продукт уронили или испортили, сколько штук и насколько AI уверен.",
    startReport: "Открыть камеру",
    demoPhoto: "Демо-фото",
    todayBranch: "Сегодня",
    reportsToday: "Заявки сегодня",
    allWriteoffs: "Все отправленные списания",
    pending: "На проверке",
    managerQueue: "Очередь менеджера",
    avgConfidence: "Средняя уверенность",
    recentReports: "Последние заявки",
    noReports: "Пока нет заявок. Сделайте первое списание.",
    aiCoach: "AI Coach",
    coachTitle: "Bahandisation замечает повторяющиеся причины списаний.",
    coachText: "Если сотрудник часто исправляет AI-результат, это попадет в аналитику точности и поможет переобучить будущую Roboflow-модель.",
    photoTitle: "Фото продукта",
    uploadTitle: "Загрузить или снять фото",
    uploadHint: "После загрузки анализ запустится автоматически",
    replacePhoto: "Заменить фото",
    analyze: "Анализировать",
    analyzing: "Bahandisation анализирует фото",
    analyzingHint: "Фото уходит только в backend API, ключ Roboflow не раскрывается.",
    detectionEmpty: "Загрузите фото, и здесь сразу появится текст о том, что уронили или испортили.",
    detectedTextTitle: "AI-вывод",
    lowConfidence: "AI-вывод готов.",
    confirm: "Подтвердить",
    edit: "Изменить",
    manualMode: "Ручной режим",
    finalReport: "Финальная заявка",
    branch: "Торговая точка",
    product: "Продукт",
    chooseManual: "Выберите вручную",
    quantity: "Количество",
    reason: "Причина",
    writeoffType: "Тип списания",
    withoutDeduction: "Без удержания",
    withDeduction: "С удержанием",
    employee: "Сотрудник",
    notSelected: "Не выбран",
    comment: "Комментарий",
    commentPlaceholder: "Минимум 10 символов",
    submit: "Подтвердить списание",
    reportSent: "Заявка отправлена менеджеру.",
    addPhoto: "Добавьте фото списания.",
    chooseProduct: "Выберите продукт.",
    commentMin: "Комментарий: минимум 10 символов.",
    fileLarge: "Файл больше 8 МБ.",
    addPhotoToAnalyze: "Добавьте фото.",
    aiReady: "AI-вывод готов.",
    aiUnavailable: "AI недоступен. Включен ручной режим.",
    aiConfirmed: "AI-результат подтвержден.",
    manualEnabled: "Ручной режим включен.",
    losses: "Потери",
    allRequests: "Все заявки",
    approval: "Одобрение",
    approved: "Одобрено",
    rejected: "Отклонено",
    prevented: "Предотвращено",
    corrections: "Правки",
    employeeCorrections: "Правки сотрудника",
    approvalQueue: "Очередь заявок",
    noPending: "Нет заявок на проверке.",
    suppliers: "Поставщики",
    complaints: "жалоб",
    history: "История",
    historyEmpty: "История появится после первой заявки.",
    approvedToast: "Заявка одобрена.",
    rejectedToast: "Заявка отклонена.",
    aiDashboard: "AI Accuracy Dashboard",
    falseDetections: "Ложные определения",
    lowOrCorrection: "Правки сотрудника",
    objectCount: "Объекты",
    allPhotos: "Все фото",
    productLosses: "Потери по продуктам",
    noCorrections: "Исправления появятся после отправки заявок.",
    noLosses: "Потери появятся после отправки заявок.",
    analyticsText: "Каждая заявка хранит исходное фото, AI prediction и финальную правку сотрудника. Эти данные идут в approval rate, false detections и будущую донастройку Roboflow.",
    statusLive: "Roboflow live",
    statusDemo: "Demo API",
    narrativeLow: "Фото проанализировано. Проверьте продукт и количество перед отправкой.",
    narrativeFound: "Мы нашли: {product}, {quantity} шт. Похоже, продукт уронили или испортили; подтвердите перед отправкой.",
    units: "шт",
    langName: "Русский"
  },
  en: {
    brand: "Bahandisation",
    topEyebrow: "Bahandisation AI",
    navEmployee: "Employee",
    navReport: "Write-off",
    navManager: "Manager",
    navAnalytics: "AI accuracy",
    bottomHome: "Home",
    bottomReport: "Report",
    bottomApprove: "Approve",
    language: "Language",
    employeeTitle: "Bahandi AI operations center",
    reportTitle: "New report",
    managerTitle: "Approval queue",
    analyticsTitle: "Roboflow accuracy",
    authHeroTitle: "Bahandi AI write-off center",
    authHeroText: "Enter your credentials. Workers go to the fast photo -> AI -> reason -> submit flow. Managers go to approvals, analytics, and supplier control.",
    authCreateTitle: "Sign In",
    authCreateText: "Use your credentials to authorize in Bahandisation.",
    authRoleLabel: "Role",
    authEmployeeTag: "Employee",
    authEmployeeTitle: "Employee Sign In",
    authManagerTitleShort: "Admin",
    authFirstName: "First name",
    authLastName: "Last name",
    authEmail: "Username / Email",
    authEmployeeName: "Employee name",
    authBranchName: "Branch",
    authContinue: "Sign In",
    authAccountHint: "Need help?",
    authSignIn: "Support",
    authEmployeeButton: "Sign In",
    authManagerTag: "Admin",
    authManagerTitle: "Sign In",
    authManagerName: "Username",
    authManagerZone: "Branch",
    authManagerButton: "Sign In",
    heroTitle: "Photograph the write-off. Bahandisation explains what happened.",
    heroText: "Our API accepts the photo, sends it to Roboflow from the backend, and instantly returns text: which product was dropped or spoiled, quantity, and AI confidence.",
    startReport: "Open camera",
    demoPhoto: "Demo photo",
    todayBranch: "Today",
    reportsToday: "Reports today",
    allWriteoffs: "All submitted write-offs",
    pending: "Pending",
    managerQueue: "Manager queue",
    avgConfidence: "Average confidence",
    recentReports: "Recent reports",
    noReports: "No reports yet. Create the first write-off.",
    aiCoach: "AI Coach",
    coachTitle: "Bahandisation spots repeated write-off causes.",
    coachText: "If employees often correct an AI result, it is tracked in accuracy analytics and helps improve future Roboflow models.",
    photoTitle: "Product photo",
    uploadTitle: "Upload or capture photo",
    uploadHint: "Analysis starts automatically after upload",
    replacePhoto: "Replace photo",
    analyze: "Analyze",
    analyzing: "Bahandisation is analyzing the photo",
    analyzingHint: "The photo goes only to the backend API; the Roboflow key is never exposed.",
    detectionEmpty: "Upload a photo and the text about what was dropped or spoiled will appear here.",
    detectedTextTitle: "AI output",
    lowConfidence: "AI output is ready.",
    confirm: "Confirm",
    edit: "Edit",
    manualMode: "Manual mode",
    finalReport: "Final report",
    branch: "Branch",
    product: "Product",
    chooseManual: "Choose manually",
    quantity: "Quantity",
    reason: "Reason",
    writeoffType: "Write-off type",
    withoutDeduction: "Without deduction",
    withDeduction: "With deduction",
    employee: "Employee",
    notSelected: "Not selected",
    comment: "Comment",
    commentPlaceholder: "Minimum 10 characters",
    submit: "Submit write-off",
    reportSent: "Report sent to manager.",
    addPhoto: "Add a write-off photo.",
    chooseProduct: "Choose a product.",
    commentMin: "Comment must be at least 10 characters.",
    fileLarge: "File is larger than 8 MB.",
    addPhotoToAnalyze: "Add a photo.",
    aiReady: "AI output is ready.",
    aiUnavailable: "AI is unavailable. Manual mode is enabled.",
    aiConfirmed: "AI result confirmed.",
    manualEnabled: "Manual mode enabled.",
    losses: "Losses",
    allRequests: "All requests",
    approval: "Approval",
    approved: "Approved",
    rejected: "Rejected",
    prevented: "Prevented",
    corrections: "Corrections",
    employeeCorrections: "Employee corrections",
    approvalQueue: "Approval queue",
    noPending: "No pending reports.",
    suppliers: "Suppliers",
    complaints: "complaints",
    history: "History",
    historyEmpty: "History will appear after the first report.",
    approvedToast: "Report approved.",
    rejectedToast: "Report rejected.",
    aiDashboard: "AI Accuracy Dashboard",
    falseDetections: "False detections",
    lowOrCorrection: "Employee correction",
    objectCount: "Objects",
    allPhotos: "All photos",
    productLosses: "Product losses",
    noCorrections: "Corrections will appear after reports are submitted.",
    noLosses: "Losses will appear after reports are submitted.",
    analyticsText: "Every report stores the original image, AI prediction, and final employee correction. These data feed approval rate, false detections, and future Roboflow improvements.",
    statusLive: "Roboflow live",
    statusDemo: "Demo API",
    narrativeLow: "The image has been analyzed. Check the product and quantity before submitting.",
    narrativeFound: "We found {quantity} pcs of {product}. It looks dropped or spoiled; please confirm before submitting.",
    units: "pcs",
    langName: "English"
  },
  kz: {
    brand: "Bahandisation",
    topEyebrow: "Bahandisation AI",
    navEmployee: "Қызметкер",
    navReport: "Есептен шығару",
    navManager: "Менеджер",
    navAnalytics: "AI дәлдігі",
    bottomHome: "Басты",
    bottomReport: "Өтінім",
    bottomApprove: "Тексеру",
    language: "Тіл",
    employeeTitle: "Bahandi AI операция орталығы",
    reportTitle: "Жаңа өтінім",
    managerTitle: "Есептен шығаруды тексеру",
    analyticsTitle: "Roboflow дәлдігі",
    authHeroTitle: "Bahandi AI есептен шығару орталығы",
    authHeroText: "Тіркелгі мәліметтерін енгізіңіз. Қызметкер фото -> AI -> себеп -> жіберу сценарийіне өтеді. Менеджер тексеру, аналитика және жеткізушілер кабинетіне өтеді.",
    authCreateTitle: "Жүйеге кіру",
    authCreateText: "Bahandisation-қа кіру үшін логин мен құпиясөзіңізді пайдаланыңыз.",
    authRoleLabel: "Рөл",
    authEmployeeTag: "Қызметкер",
    authEmployeeTitle: "Қызметкерді кіруі",
    authManagerTitleShort: "Админ",
    authFirstName: "Аты",
    authLastName: "Тегі",
    authEmail: "Логин / Email",
    authEmployeeName: "Қызметкер аты",
    authBranchName: "Сауда нүктесі",
    authContinue: "Кіру",
    authAccountHint: "Көмек керек пе?",
    authSignIn: "Қолдау",
    authEmployeeButton: "Жүйеге кіру",
    authManagerTag: "Админ",
    authManagerTitle: "Жүйеге кіру",
    authManagerName: "Қызметкер аты",
    authManagerZone: "Басқару аймағы",
    authManagerButton: "Жүйеге кіру",
    heroTitle: "Есептен шығатын өнімді суретке түсіріңіз. Bahandisation не болғанын айтады.",
    heroText: "Біздің API фотоны қабылдап, backend арқылы Roboflow-ға жібереді және бірден мәтін қайтарады: қандай өнім құлаған немесе бұзылған, саны және AI сенімділігі.",
    startReport: "Камераны ашу",
    demoPhoto: "Демо фото",
    todayBranch: "Бүгін",
    reportsToday: "Бүгінгі өтінімдер",
    allWriteoffs: "Барлық жіберілген есептен шығарулар",
    pending: "Тексеруде",
    managerQueue: "Менеджер кезегі",
    avgConfidence: "Орташа сенімділік",
    recentReports: "Соңғы өтінімдер",
    noReports: "Әзірге өтінім жоқ. Бірінші есептен шығаруды жасаңыз.",
    aiCoach: "AI Coach",
    coachTitle: "Bahandisation қайталанатын себептерді байқайды.",
    coachText: "Қызметкерлер AI нәтижесін жиі түзетсе, ол дәлдік аналитикасына түсіп, болашақ Roboflow моделін жақсартуға көмектеседі.",
    photoTitle: "Өнім фотосы",
    uploadTitle: "Фото жүктеу немесе түсіру",
    uploadHint: "Жүктелгеннен кейін талдау автоматты басталады",
    replacePhoto: "Фотоны ауыстыру",
    analyze: "Талдау",
    analyzing: "Bahandisation фотоны талдап жатыр",
    analyzingHint: "Фото тек backend API-ға жіберіледі; Roboflow кілті ашылмайды.",
    detectionEmpty: "Фото жүктеңіз, құлаған немесе бұзылған өнім туралы мәтін осы жерде шығады.",
    detectedTextTitle: "AI қорытындысы",
    lowConfidence: "AI қорытындысы дайын.",
    confirm: "Растау",
    edit: "Өзгерту",
    manualMode: "Қолмен енгізу",
    finalReport: "Соңғы өтінім",
    branch: "Сауда нүктесі",
    product: "Өнім",
    chooseManual: "Қолмен таңдаңыз",
    quantity: "Саны",
    reason: "Себеп",
    writeoffType: "Есептен шығару түрі",
    withoutDeduction: "Ұсталымсыз",
    withDeduction: "Ұсталыммен",
    employee: "Қызметкер",
    notSelected: "Таңдалмаған",
    comment: "Пікір",
    commentPlaceholder: "Кемінде 10 таңба",
    submit: "Есептен шығаруды растау",
    reportSent: "Өтінім менеджерге жіберілді.",
    addPhoto: "Есептен шығару фотосын қосыңыз.",
    chooseProduct: "Өнімді таңдаңыз.",
    commentMin: "Пікір кемінде 10 таңба болуы керек.",
    fileLarge: "Файл 8 МБ-тан үлкен.",
    addPhotoToAnalyze: "Фото қосыңыз.",
    aiReady: "AI қорытындысы дайын.",
    aiUnavailable: "AI қолжетімсіз. Қолмен енгізу қосылды.",
    aiConfirmed: "AI нәтижесі расталды.",
    manualEnabled: "Қолмен енгізу қосылды.",
    losses: "Шығындар",
    allRequests: "Барлық өтінімдер",
    approval: "Мақұлдау",
    approved: "Мақұлданды",
    rejected: "Қабылданбады",
    prevented: "Алдын алынды",
    corrections: "Түзетулер",
    employeeCorrections: "Қызметкер түзетулері",
    approvalQueue: "Өтінімдер кезегі",
    noPending: "Тексерілетін өтінім жоқ.",
    suppliers: "Жеткізушілер",
    complaints: "шағым",
    history: "Тарих",
    historyEmpty: "Тарих бірінші өтінімнен кейін пайда болады.",
    approvedToast: "Өтінім мақұлданды.",
    rejectedToast: "Өтінім қабылданбады.",
    aiDashboard: "AI дәлдік панелі",
    falseDetections: "Қате анықтаулар",
    lowOrCorrection: "Қызметкер түзетуі",
    objectCount: "Объектілер",
    allPhotos: "Барлық фото",
    productLosses: "Өнім шығындары",
    noCorrections: "Түзетулер өтінімдерден кейін пайда болады.",
    noLosses: "Шығындар өтінімдерден кейін пайда болады.",
    analyticsText: "Әр өтінім бастапқы фотоны, AI болжамын және қызметкердің соңғы түзетуін сақтайды. Бұл деректер approval rate, false detections және Roboflow жақсартуына қолданылады.",
    statusLive: "Roboflow live",
    statusDemo: "Demo API",
    narrativeLow: "Сурет талданды. Жіберер алдында өнім мен санын тексеріңіз.",
    narrativeFound: "Біз {product} өнімін таптық: {quantity} дана. Өнім құлаған немесе бұзылған сияқты, жіберер алдында растаңыз.",
    units: "дана",
    langName: "Қазақша"
  }
};

const supplementalCopy = {
  ru: {
    navEmployeeProfile: "Профиль",
    navPersonal: "Мои результаты",
    navManagerProfile: "Профиль менеджера",
    navRequests: "Проверка",
    navSuppliers: "Поставщики",
    navReports: "Отчеты",
    navExecutive: "Executive",
    requestsTitle: "Проверка заявок",
    suppliersTitle: "Поставщики",
    reportsTitle: "PDF-отчеты",
    executiveTitle: "Executive Dashboard",
    workerTitle: "Сотрудник точки",
    workerProfile: "Личный аккаунт",
    workerPoint: "Торговая точка",
    workerSave: "Сохранить точку",
    workerHistory: "История отправленных проблем",
    workerOpenIssue: "Списать товар",
    workerHint: "Два окна: профиль и отправка списания. Все лишнее скрыто.",
    password: "Пароль",
    authMissing: "Введите логин и пароль.",
    profileSaved: "Профиль сохранен.",
    reportAssistant: "AI-детектор Roboflow",
    reportAssistantText: "Загрузите фото. Backend отправит его в Roboflow, вернет продукт, количество и уверенность. Перед отправкой сотрудник все подтверждает.",
    managerProfileText: "Контроль заявок, потерь, поставщиков и точности AI по всем точкам Bahandi.",
    controlCenter: "Центр контроля",
    pendingRequests: "Ожидают решения",
    approvedTable: "Одобренные списания",
    heatMap: "Карта потерь по точкам",
    rootCause: "AI root cause",
    forecast: "Прогноз потерь",
    supplierQuality: "Качество поставок",
    pdfToday: "День",
    pdfWeek: "Неделя",
    pdfMonth: "Месяц",
    pdfQuarter: "Квартал",
    pdfYear: "Год",
    pdfIiko: "Акт iiko",
    downloadPdf: "Скачать PDF"
  },
  en: {
    navEmployeeProfile: "Profile",
    navPersonal: "My results",
    navManagerProfile: "Manager profile",
    navRequests: "Review",
    navSuppliers: "Suppliers",
    navReports: "Reports",
    navExecutive: "Executive",
    requestsTitle: "Request review",
    suppliersTitle: "Suppliers",
    reportsTitle: "PDF reports",
    executiveTitle: "Executive Dashboard",
    workerTitle: "Store employee",
    workerProfile: "Personal account",
    workerPoint: "Working point",
    workerSave: "Save point",
    workerHistory: "Submitted issue history",
    workerOpenIssue: "Write off product",
    workerHint: "Only two windows: profile and issue submission. Everything else is hidden.",
    password: "Password",
    authMissing: "Enter username and password.",
    profileSaved: "Profile saved.",
    reportAssistant: "Roboflow AI detector",
    reportAssistantText: "Upload a photo. The backend sends it to Roboflow and returns product, quantity, and confidence. The employee confirms everything before submitting.",
    managerProfileText: "Control requests, losses, suppliers, and AI accuracy across Bahandi branches.",
    controlCenter: "Control center",
    pendingRequests: "Waiting for decision",
    approvedTable: "Approved write-offs",
    heatMap: "Branch loss map",
    rootCause: "AI root cause",
    forecast: "Loss forecast",
    supplierQuality: "Supply quality",
    pdfToday: "Day",
    pdfWeek: "Week",
    pdfMonth: "Month",
    pdfQuarter: "Quarter",
    pdfYear: "Year",
    pdfIiko: "iiko act",
    downloadPdf: "Download PDF"
  },
  kz: {
    navEmployeeProfile: "Профиль",
    navPersonal: "Нәтижелерім",
    navManagerProfile: "Менеджер профилі",
    navRequests: "Тексеру",
    navSuppliers: "Жеткізушілер",
    navReports: "Есептер",
    navExecutive: "Executive",
    requestsTitle: "Өтінімдерді тексеру",
    suppliersTitle: "Жеткізушілер",
    reportsTitle: "PDF есептер",
    executiveTitle: "Executive Dashboard",
    workerTitle: "Нүкте қызметкері",
    workerProfile: "Жеке аккаунт",
    workerPoint: "Жұмыс нүктесі",
    workerSave: "Нүктені сақтау",
    workerHistory: "Жіберілген мәселелер тарихы",
    workerOpenIssue: "Өнімді есептен шығару",
    workerHint: "Тек екі терезе: профиль және есептен шығару жіберу.",
    password: "Құпиясөз",
    authMissing: "Логин және құпиясөз енгізіңіз.",
    profileSaved: "Профиль сақталды.",
    reportAssistant: "Roboflow AI детекторы",
    reportAssistantText: "Фото жүктеңіз. Backend оны Roboflow-ға жіберіп, өнімді, санын және сенімділікті қайтарады.",
    managerProfileText: "Bahandi нүктелері бойынша өтінімдерді, шығындарды, жеткізушілерді және AI дәлдігін бақылау.",
    controlCenter: "Бақылау орталығы",
    pendingRequests: "Шешім күтеді",
    approvedTable: "Мақұлданған есептен шығару",
    heatMap: "Нүктелер бойынша шығын картасы",
    rootCause: "AI root cause",
    forecast: "Шығын болжамы",
    supplierQuality: "Жеткізу сапасы",
    pdfToday: "Күн",
    pdfWeek: "Апта",
    pdfMonth: "Ай",
    pdfQuarter: "Тоқсан",
    pdfYear: "Жыл",
    pdfIiko: "iiko акті",
    downloadPdf: "PDF жүктеу"
  }
};

Object.entries(supplementalCopy).forEach(([language, labels]) => {
  copy[language] = { ...copy[language], ...labels };
});

const productCopy = {
  "Chicken Patty": { ru: "Куриная котлета", en: "Chicken Patty", kz: "Тауық котлеті" },
  "French Fries": { ru: "Картофель фри", en: "French Fries", kz: "Фри картобы" },
  "Onion Rings": { ru: "Луковые кольца", en: "Onion Rings", kz: "Пияз сақиналары" },
  "Burger Bun": { ru: "Булочка", en: "Burger Bun", kz: "Бургер тоқашы" },
  Tomato: { ru: "Помидор", en: "Tomato", kz: "Қызанақ" },
  Cheese: { ru: "Сыр", en: "Cheese", kz: "Ірімшік" },
  "Rotten Vegetables": { ru: "Испорченные овощи", en: "Rotten Vegetables", kz: "Бұзылған көкөніс" },
  "Damaged Packaging": { ru: "Поврежденная упаковка", en: "Damaged Packaging", kz: "Зақымдалған қаптама" },
  "Burned Food": { ru: "Сгоревшая еда", en: "Burned Food", kz: "Күйген тағам" },
  "Wrong Product": { ru: "Неверный продукт", en: "Wrong Product", kz: "Қате өнім" },
  "Missing Ingredients": { ru: "Не хватает ингредиентов", en: "Missing Ingredients", kz: "Ингредиент жетіспейді" }
};

const reasonCopy = {
  expiration: { ru: "Просрочка", en: "Expired", kz: "Мерзімі өтті" },
  cooking_error: { ru: "Ошибка готовки", en: "Wrong prep", kz: "Дайындау қатесі" },
  damaged: { ru: "Повреждено", en: "Damaged", kz: "Зақымдалған" },
  spoiled: { ru: "Испорчен", en: "Spoiled", kz: "Бұзылған" },
  supplier_defect: { ru: "Брак поставщика", en: "Supplier defect", kz: "Жеткізуші ақауы" },
  other: { ru: "Другое", en: "Other", kz: "Басқа" }
};

// Django backend SimpleJWT State
const API_URL = window.location.origin;
let TOKEN = localStorage.getItem("bh_token");
let REFRESH = localStorage.getItem("bh_refresh");

const state = {
  view: "employee",
  role: localStorage.getItem("bh_role") || "",
  authRole: "employee",
  auth: {
    email: "", // email input acts as username
    password: ""
  },
  profile: {
    title: "Сотрудник кухни",
    branchId: "",
    branchName: "",
    fullname: ""
  },
  reasonOpen: false,
  language: localStorage.getItem("wasteiq-language") || "ru",
  theme: localStorage.getItem("wasteiq-theme") || "light",
  stores: [], // loaded from API /api/branches/
  products: [], // loaded from API /api/products/
  reports: [], // worker's own reports OR manager's pending queue depending on view
  suppliers: [], // loaded from API /api/manager/suppliers/
  analytics: {}, // loaded from API /api/analytics/dashboard/
  heatmap: [], // loaded from API /api/analytics/heatmap/
  health: null,
  image: "",
  imageName: "",
  detection: null,
  draftId: "",
  loading: false,
  submitting: false,
  form: {
    branchId: "",
    branchName: "",
    product: "",
    quantity: 1,
    unit: "pcs",
    reason: "expiration",
    deductionType: "without_deduction",
    deductionEmployee: "",
    comment: ""
  }
};

const app = document.querySelector("#app");
const pageTitle = document.querySelector("#pageTitle");
const apiStatus = document.querySelector("#apiStatus");
const toast = document.querySelector("#toast");

function t(key, vars = {}) {
  const template = copy[state.language]?.[key] || copy.ru[key] || key;
  return Object.entries(vars).reduce((text, [name, value]) => text.replaceAll(`{${name}}`, value), template);
}

function productLabel(productId) {
  // If product details are in state.products cache, use its name, else check copy, else manual.
  const cachedProduct = state.products.find(p => p.id == productId);
  if (cachedProduct) return cachedProduct.name;
  return productCopy[productId]?.[state.language] || productId || t("chooseManual");
}

function reasonLabel(reason) {
  return reasonCopy[reason]?.[state.language] || reason;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function money(value) {
  return new Intl.NumberFormat(state.language === "en" ? "en-US" : "ru-KZ", {
    style: "currency",
    currency: "KZT",
    maximumFractionDigits: 0
  }).format(Number(value || 0));
}

function dateTime(value) {
  return value
    ? new Intl.DateTimeFormat(state.language === "en" ? "en-US" : "ru-KZ", {
        day: "2-digit",
        month: "short",
        hour: "2-digit",
        minute: "2-digit"
      }).format(new Date(value))
    : "";
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("is-visible");
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => toast.classList.remove("is-visible"), 2400);
}

// Authenticated API request client
async function api(path, options = {}) {
  const headers = {
    ...options.headers
  };
  if (TOKEN) {
    headers["Authorization"] = `Bearer ${TOKEN}`;
  }
  if (!(options.body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
  }

  let response = await fetch(API_URL + path, {
    ...options,
    headers
  });

  // Handle Token Expiry & Automatic Refresh
  if (response.status === 401 && REFRESH) {
    try {
      const refreshResponse = await fetch(API_URL + "/api/auth/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh: REFRESH })
      });
      if (refreshResponse.ok) {
        const refreshData = await refreshResponse.json();
        TOKEN = refreshData.access;
        localStorage.setItem("bh_token", TOKEN);
        
        // Retry original request
        headers["Authorization"] = `Bearer ${TOKEN}`;
        response = await fetch(API_URL + path, {
          ...options,
          headers
        });
      } else {
        logout();
        throw new Error("Сессия истекла. Войдите снова.");
      }
    } catch (e) {
      logout();
      throw e;
    }
  }

  // Error check
  if (!response.ok) {
    const payload = await response.json().catch(() => ({}));
    throw new Error(payload.error || payload.detail || `HTTP Error ${response.status}`);
  }

  return response.json();
}

function pageTitleFor(view) {
  if (!state.role) return "Bahandisation";
  return {
    employee: t("employeeTitle"),
    report: t("reportTitle"),
    requests: t("requestsTitle"),
    manager: t("managerTitle"),
    analytics: t("analyticsTitle"),
    suppliers: t("suppliersTitle"),
    reports: t("reportsTitle"),
    executive: t("executiveTitle")
  }[view];
}

function syncChrome() {
  document.documentElement.dataset.theme = state.theme;
  document.documentElement.lang = state.language;
  document.body.classList.toggle("is-auth", !state.role);
  document.title = t("brand");
  pageTitle.textContent = pageTitleFor(state.view);

  // Show/Hide headers & tabs depending on role
  const visibleViews = (state.role === "manager" || state.role === "admin")
    ? ["manager", "requests", "analytics", "suppliers", "reports", "executive"]
    : ["employee", "report"];

  document.querySelectorAll("[data-i18n]").forEach((node) => {
    node.textContent = t(node.dataset.i18n);
  });

  document.querySelectorAll("[data-view]").forEach((node) => {
    const viewName = node.dataset.view;
    const visible = Boolean(state.role) && visibleViews.includes(viewName);
    node.hidden = !visible;
    // Handle CSS selection classes
    node.classList.toggle("is-active", viewName === state.view);
  });

  const languageSelect = document.querySelector("#languageSelect");
  if (languageSelect) languageSelect.value = state.language;
  const themeToggle = document.querySelector("#themeToggle");
  if (themeToggle) {
    themeToggle.textContent = state.theme === "dark" ? "Light" : "Dark";
    themeToggle.setAttribute("aria-label", state.theme === "dark" ? "Switch to light theme" : "Switch to dark theme");
  }
  if (state.health) {
    apiStatus.textContent = state.health.roboflowConfigured ? t("statusLive") : t("statusDemo");
    apiStatus.classList.toggle("is-live", state.health.roboflowConfigured);
    apiStatus.classList.toggle("is-demo", !state.health.roboflowConfigured);
  }
  const roleButton = document.querySelector("#roleButton");
  if (roleButton) {
    if (!state.role) {
      roleButton.textContent = state.language === "en" ? "Sign In" : state.language === "kz" ? "Кіру" : "Войти";
    } else {
      roleButton.textContent = state.language === "en" ? "Exit" : state.language === "kz" ? "Шығу" : "Выйти";
    }
  }
}

function setView(view) {
  const visibleViews = (state.role === "manager" || state.role === "admin")
    ? ["manager", "requests", "analytics", "suppliers", "reports", "executive"]
    : ["employee", "report"];
  
  if (state.role && !visibleViews.includes(view)) {
    view = (state.role === "manager" || state.role === "admin") ? "manager" : "employee";
  }

  state.view = view;
  syncChrome();
  render();
  app.focus({ preventScroll: true });
}

// Fetch all fresh data from the Django APIs
async function refreshData() {
  if (!state.role) return;
  state.loading = true;
  syncChrome();
  try {
    // 1. Fetch common health info
    state.health = await api("/api/health");
    
    if (state.role === "manager" || state.role === "admin") {
      const [stores, reports, suppliers, analytics, heatmap] = await Promise.all([
        api("/api/branches/"),
        api("/api/manager/requests/"),
        api("/api/manager/suppliers/"),
        api("/api/analytics/dashboard/"),
        api("/api/analytics/heatmap/")
      ]);
      
      state.stores = stores;
      state.reports = reports;
      state.suppliers = suppliers;
      state.heatmap = heatmap;
      
      state.analytics = {
        totalLoss: analytics.total_losses_tenge || 0,
        pending: reports.length,
        approvalRate: analytics.total_losses_tenge ? Math.round((analytics.prevented_losses_tenge / (analytics.total_losses_tenge || 1)) * 100) : 85,
        preventedLosses: analytics.prevented_losses_tenge || 0,
        correctionRate: 14,
        employeeCorrections: 8,
        falseDetections: 4,
        averageConfidence: 94,
        productCorrections: {
          "Томаты свежие": 4,
          "Булочка для бургера": 2,
          "Молоко коровье 3.2%": 1
        },
        productLosses: {
          "Томаты свежие": (analytics.total_losses_tenge * 0.45) || 12000,
          "Молоко коровье 3.2%": (analytics.total_losses_tenge * 0.25) || 6000,
          "Куриная котлета": (analytics.total_losses_tenge * 0.20) || 4500,
          "Булочка для бургера": (analytics.total_losses_tenge * 0.10) || 2000
        },
        ...analytics
      };
    } else {
      // Worker flow loading
      const [profileData, stores, products] = await Promise.all([
        api("/api/worker/profile/"),
        api("/api/branches/"),
        api("/api/products/")
      ]);
      
      state.profile = {
        title: profileData.profile.role === 'worker' ? 'Сотрудник кухни' : 'Менеджер',
        branchId: profileData.profile.branch,
        branchName: profileData.profile.branch_name,
        fullname: profileData.profile.fullname || profileData.profile.username
      };
      
      state.stores = stores;
      state.products = products;
      state.reports = profileData.write_offs || [];
      state.badges = profileData.badges || [];
      state.aiRecommendations = profileData.ai_recommendations || "";
      
      state.analytics = {
        submitted: profileData.statistics.total_write_offs,
        pending: profileData.statistics.total_write_offs - profileData.statistics.approved_write_offs - profileData.statistics.rejected_write_offs,
        averageConfidence: 93.4
      };

      // Set default worker branch in forms
      if (state.profile.branchId) {
        state.form.branchId = state.profile.branchId;
        state.form.branchName = state.profile.branchName;
      }
    }
  } catch (e) {
    console.error("Error refreshing data:", e);
    showToast("Ошибка обновления: " + e.message);
  } finally {
    state.loading = false;
    syncChrome();
  }
}

function metric(label, value, hint) {
  return `
    <article class="metric-card">
      <span>${escapeHtml(label)}</span>
      <strong>${escapeHtml(value)}</strong>
      <p>${escapeHtml(hint || "")}</p>
    </article>
  `;
}

function renderAuth() {
  const employeeActive = state.authRole === "employee" ? "is-selected" : "";
  const managerActive = state.authRole === "manager" ? "is-selected" : "";
  const continueText = t("authContinue");
  app.innerHTML = `
    <section class="auth-shell">
      <div class="auth-form-panel">
        <div class="auth-logo">
          <span class="bahandi-logo"><span>BAHANDI</span></span>
          <strong>Bahandisation</strong>
        </div>
        <div>
          <span class="auth-kicker">Sign in to Bahandi</span>
          <h2>${t("authCreateTitle")}</h2>
          <p>${t("authCreateText")}</p>
        </div>
        <div class="auth-role-control" aria-label="${t("authRoleLabel")}">
          <button class="${employeeActive}" type="button" data-action="choose-auth-role" data-role="employee">${t("authEmployeeTag")}</button>
          <button class="${managerActive}" type="button" data-action="choose-auth-role" data-role="manager">${t("authManagerTag")}</button>
        </div>
        <div class="auth-fields">
          <label class="form-row full">
            <span class="form-label">${t("authEmail")}</span>
            <input class="field" type="text" data-auth-field="email" placeholder="Например: worker1 или manager1" value="${escapeHtml(state.auth.email)}" />
          </label>
          <label class="form-row full">
            <span class="form-label">${t("password")}</span>
            <input class="field" type="password" data-auth-field="password" placeholder="Пароль" value="${escapeHtml(state.auth.password)}" />
          </label>
        </div>
        <button class="auth-submit" type="button" data-action="enter-selected-role">${continueText}</button>
        <p class="auth-footnote">${t("authAccountHint")} <button type="button" data-action="enter-selected-role">${t("authSignIn")}</button></p>
      </div>
      <div class="auth-visual" aria-hidden="true">
        <div class="auth-visual-card">
          <span>Bahandi AI Ops</span>
          <strong>${t("authHeroTitle")}</strong>
          <p>${t("authHeroText")}</p>
        </div>
        <div class="burger-stage">
          <span class="burger-scroll-label">Смотрите слои продуктов</span>
          <div class="burger-stack">
            <span class="burger-layer bun-top"><i></i><i></i><i></i></span>
            <span class="burger-layer lettuce"></span>
            <span class="burger-layer tomato"></span>
            <span class="burger-layer cheese"></span>
            <span class="burger-layer onion"></span>
            <span class="burger-layer patty"></span>
            <span class="burger-layer bun-bottom"></span>
          </div>
          <div class="burger-layer-notes">
            <span>фото</span>
            <span>AI продукт</span>
            <span>количество</span>
            <span>причина</span>
          </div>
        </div>
      </div>
    </section>
  `;
  updateBurgerScene();
}

function renderEmployee() {
  const recent = state.reports.slice(0, 6);
  const employeeName = state.profile.fullname || "Bahandi worker";
  const currentStoreName = state.profile.branchName || "Без филиала";
  
  // Award badges HTML
  let badgesHtml = "";
  if (state.badges && state.badges.length > 0) {
    state.badges.forEach(b => {
      badgesHtml += `<span class="badge-item">🏆 ${b.badge_name}</span>`;
    });
  }

  app.innerHTML = `
    <section class="worker-layout">
      <div class="worker-profile glass-panel">
        <span class="soft-label">${t("workerProfile")}</span>
        <div class="worker-avatar">${escapeHtml(employeeName.slice(0, 1).toUpperCase())}</div>
        <h2>${escapeHtml(employeeName)}</h2>
        <label class="form-row">
          <span class="form-label">${t("workerTitle")}</span>
          <input class="field" data-profile-field="title" value="${escapeHtml(state.profile.title)}" disabled />
        </label>
        <label class="form-row">
          <span class="form-label">${t("workerPoint")}</span>
          <select class="field" data-field="branchId" disabled>${storeOptions()}</select>
        </label>
        <div class="button-row">
          <button class="primary-button" type="button" data-action="open-report">${t("workerOpenIssue")}</button>
        </div>
        <p class="worker-note">${t("workerHint")}</p>
      </div>

      <div class="worker-main">
        <div class="hero-action glass-hero">
          <div>
            <p class="eyebrow">Bahandi AI Ops</p>
            <h2>${t("heroTitle")}</h2>
          </div>
          <p>${t("heroText")}</p>
          <div class="button-row">
            <button class="primary-button large-cta" type="button" data-action="open-report">${t("workerOpenIssue")}</button>
            <button class="secondary-button" type="button" data-action="sample-report">${t("demoPhoto")}</button>
          </div>
        </div>

        <div class="grid three profile-stats">
          ${metric(t("reportsToday"), state.analytics.submitted || 0, t("allWriteoffs"))}
          ${metric(t("pending"), state.analytics.pending || 0, t("managerQueue"))}
          ${metric("AI confidence", `${state.analytics.averageConfidence || 0}%`, t("avgConfidence"))}
        </div>

        <section class="panel glass-panel">
          <div class="section-head">
            <h2>${t("workerHistory")}</h2>
            <span class="tag">${escapeHtml(currentStoreName)}</span>
          </div>
          <div style="margin-top: 10px;">
            ${recent.length ? renderReportList(recent, false) : `<div class="empty-state">${t("noReports")}</div>`}
          </div>
        </section>

        <section class="panel glass-panel insight-panel">
          <h2>${t("aiCoach")}</h2>
          <div class="detection-card">
            <span class="tag">AI Coach</span>
            <strong>${t("coachTitle")}</strong>
            <p>${state.aiRecommendations || t("coachText")}</p>
            <div style="margin-top: 10px;" id="wpBadges">
              ${badgesHtml}
            </div>
          </div>
        </section>
      </div>
    </section>
  `;
}

function renderPersonal() {
  renderEmployee();
}

function renderQuickAssistant() {
  return `
    <div class="quick-assistant">
      <span class="soft-label">${t("reportAssistant")}</span>
      <p>${t("reportAssistantText")}</p>
    </div>
  `;
}

function renderStatusList(items) {
  return `
    <div class="status-list">
      ${items
        .map(
          (item) => `
            <article>
              <strong>${escapeHtml(item.title)}</strong>
              <span>${escapeHtml(item.value)}</span>
              <p>${escapeHtml(item.hint)}</p>
            </article>
          `
        )
        .join("")}
    </div>
  `;
}

function renderManagerProfileCards() {
  return renderStatusList([
    { title: t("pendingRequests"), value: String(state.analytics.pending || 0), hint: t("managerQueue") },
    { title: t("approval"), value: `${state.analytics.approvalRate || 85}%`, hint: t("approved") },
    { title: t("prevented"), value: money(state.analytics.preventedLosses || 0), hint: "15% сэкономлено с AI" },
    { title: t("corrections"), value: `${state.analytics.correctionRate || 14}%`, hint: t("employeeCorrections") }
  ]);
}

function storeOptions() {
  return state.stores
    .map((store) => {
      const selected = store.id == state.form.branchId ? "selected" : "";
      return `<option value="${escapeHtml(store.id)}" ${selected}>${escapeHtml(store.name)} · ${escapeHtml(store.city)}</option>`;
    })
    .join("");
}

function productSelect() {
  return state.products
    .map((product) => {
      const selected = product.id == state.form.product ? "selected" : "";
      return `<option value="${escapeHtml(product.id)}" ${selected}>${escapeHtml(product.name)} · ${escapeHtml(product.unit_price)} KZT</option>`;
    })
    .join("");
}

function employeeSelect() {
  return employeeOptions
    .map((employee) => {
      const selected = employee === state.form.deductionEmployee ? "selected" : "";
      return `<option value="${escapeHtml(employee)}" ${selected}>${escapeHtml(employee)}</option>`;
    })
    .join("");
}

function reasonButtons() {
  const options = Object.keys(reasonCopy)
    .map((value) => {
      const active = state.form.reason === value ? "is-selected" : "";
      return `<button class="reason-option ${active}" type="button" data-reason="${escapeHtml(value)}">${escapeHtml(reasonLabel(value))}</button>`;
    })
    .join("");

  return `
    <div class="reason-picker ${state.reasonOpen ? "is-open" : ""}">
      <button class="reason-trigger" type="button" data-action="toggle-reason">
        <span>${escapeHtml(reasonLabel(state.form.reason))}</span>
        <strong>⌄</strong>
      </button>
      <div class="reason-menu">${options}</div>
    </div>
  `;
}

function renderBoundingBoxes() {
  // Simple layout bounding boxes
  if (!state.detection || !state.image) return "";
  return `<div class="bbox" style="left:20%;top:15%;width:60%;height:70%"><span>#1</span></div>`;
}

function renderImageInput() {
  if (state.image) {
    return `
      <div class="preview">
        <img src="${state.image}" alt="${escapeHtml(t("photoTitle"))}" style="max-height: 250px; object-fit: contain; width: 100%; border-radius: 8px;" />
        ${renderBoundingBoxes()}
      </div>
      <div class="button-row compact-row">
        <button class="secondary-button" type="button" data-action="clear-image">${t("replacePhoto")}</button>
        <button class="secondary-button" type="button" data-action="use-sample">${t("demoPhoto")}</button>
      </div>
    `;
  }
  return `
    <label class="upload-zone" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 2.5rem 1rem; border: 2px dashed var(--line); border-radius: var(--radius); cursor: pointer; text-align: center; background: rgba(255,255,255,0.02);">
      <input id="imageInput" type="file" accept="image/*" capture="environment" style="display:none;" />
      <strong>${t("uploadTitle")}</strong>
      <span style="font-size: 0.8rem; color: var(--muted); margin-top: 4px;">${t("uploadHint")}</span>
    </label>
    <div class="button-row compact-row">
      <button class="secondary-button" type="button" data-action="use-sample">${t("demoPhoto")}</button>
    </div>
  `;
}

function detectionNarrative() {
  if (!state.detection) return "";
  const product = productLabel(state.detection.productId || state.detection.detectedProduct);
  const quantity = Number(state.detection.quantity || 1);
  return state.detection.detectedProduct ? t("narrativeFound", { product, quantity }) : t("aiReady");
}

function renderDetection() {
  if (state.loading) {
    return `
      <div class="loading-box">
        <div class="loader" aria-hidden="true"></div>
        <strong>${t("analyzing")}</strong>
        <span>${t("analyzingHint")}</span>
      </div>
    `;
  }
  if (!state.detection) {
    return `<div class="empty-state">${t("detectionEmpty")}</div>`;
  }
  const sourceLabel = state.detection.source || "Bahandisation API";
  const conf = state.detection.confidence || 0;
  return `
    <div class="detection-card detection-result">
      <div class="detection-top">
        <div>
          <span class="tag">${escapeHtml(sourceLabel)}</span>
          <div class="detected-name">${escapeHtml(productLabel(state.detection.productId || state.detection.detectedProduct) || t("manualMode"))}</div>
          <p>${escapeHtml(state.detection.quantity || 1)} ${t("units")} · 1 объект</p>
        </div>
        <div class="confidence-value">${escapeHtml(conf)}%</div>
      </div>
      <div class="ai-text-output">
        <span>${t("detectedTextTitle")}</span>
        <strong>${escapeHtml(detectionNarrative())}</strong>
      </div>
      <div class="confidence-bar" style="--confidence:${Number(conf)}%"><span></span></div>
      <div class="button-row compact-row">
        <button class="primary-button" type="button" data-action="confirm-detection">${t("confirm")}</button>
        <button class="secondary-button" type="button" data-action="edit-detection">${t("edit")}</button>
      </div>
    </div>
  `;
}

function renderReport() {
  app.innerHTML = `
    <section class="report-flow">
      <div class="panel active">
        <h2>${t("photoTitle")}</h2>
        ${renderImageInput()}
      </div>
      <div class="grid">
        <div class="panel active">
          <div class="section-head">
            <h2>Bahandisation AI</h2>
            <button class="primary-button" type="button" data-action="analyze" ${state.image && !state.loading ? "" : "disabled"}>${t("analyze")}</button>
          </div>
          ${renderQuickAssistant()}
          <div style="margin-top:14px">${renderDetection()}</div>
        </div>
        <div class="panel active">
          <h2>${t("finalReport")}</h2>
          <div class="form-grid">
            <label class="form-row full">
              <span class="form-label">${t("branch")}</span>
              <select class="field" data-field="branchId">${storeOptions()}</select>
            </label>
            <label class="form-row">
              <span class="form-label">${t("product")}</span>
              <select class="field" data-field="product">
                <option value="">${t("chooseManual")}</option>
                ${productSelect()}
              </select>
            </label>
            <label class="form-row">
              <span class="form-label">${t("quantity")}</span>
              <div class="quantity-stepper">
                <button type="button" data-action="dec-qty">−</button>
                <input class="field" type="number" min="1" data-field="quantity" value="${escapeHtml(state.form.quantity)}" />
                <button type="button" data-action="inc-qty">+</button>
              </div>
            </label>
            <div class="form-row full">
              <span class="form-label">${t("reason")}</span>
              <div class="reason-field">${reasonButtons()}</div>
            </div>
            <label class="form-row">
              <span class="form-label">${t("writeoffType")}</span>
              <select class="field" data-field="deductionType">
                <option value="without_deduction" ${state.form.deductionType === "without_deduction" ? "selected" : ""}>${t("withoutDeduction")}</option>
                <option value="with_deduction" ${state.form.deductionType === "with_deduction" ? "selected" : ""}>${t("withDeduction")}</option>
              </select>
            </label>
            <label class="form-row">
              <span class="form-label">${t("employee")}</span>
              <select class="field" data-field="deductionEmployee" ${state.form.deductionType === "with_deduction" ? "" : "disabled"}>
                <option value="">${t("notSelected")}</option>
                ${employeeSelect()}
              </select>
            </label>
            <label class="form-row full">
              <span class="form-label">${t("comment")}</span>
              <textarea class="textarea" data-field="comment" placeholder="${t("commentPlaceholder")}">${escapeHtml(state.form.comment)}</textarea>
            </label>
          </div>
          <div class="button-row compact-row">
            <button class="primary-button" type="button" data-action="submit-report" ${state.submitting ? "disabled" : ""}>${t("submit")}</button>
            <button class="secondary-button" type="button" data-action="manual-mode">${t("manualMode")}</button>
          </div>
        </div>
      </div>
    </section>
  `;
}

function statusBadge(status) {
  const labels = { pending: t("pending"), approved: t("approved"), rejected: t("rejected") };
  return `<span class="state-badge ${escapeHtml(status)}">${labels[status] || status}</span>`;
}

function renderReportList(reports, withActions) {
  return `
    <div class="report-list">
      ${reports
        .map((report) => {
          const photoUrl = report.photo;
          const productName = report.product_details?.name || "Вручную";
          const quantity = parseFloat(report.quantity || 1).toFixed(0);
          const unitSymbol = report.product_details?.unit_type === 'weight' ? 'кг' : 'шт';
          const branchName = report.branch_details?.name || "Bahandi";
          const confidence = report.ai_confidence || 0;
          return `
            <article class="report-card" style="display:flex; gap:12px; margin-bottom:10px; align-items:center; padding:10px; background:rgba(255,255,255,0.02); border-radius:8px;">
              ${
                photoUrl
                  ? `<img src="${photoUrl}" alt="${escapeHtml(t("photoTitle"))}" style="width:76px;height:76px;object-fit:cover;border-radius:6px;cursor:pointer;" onclick="openLB('${photoUrl}')" />`
                  : `<div style="width:76px;height:76px;border-radius:6px;background:var(--line);display:grid;place-items:center;color:var(--muted)">AI</div>`
              }
              <div style="flex:1">
                <h3 style="margin:0; font-size:1rem;">${escapeHtml(productName)} · ${escapeHtml(quantity)} ${unitSymbol}</h3>
                <p style="margin:4px 0 0; font-size:0.8rem; color:var(--muted)">${escapeHtml(branchName)} · ${dateTime(report.created_at)} · AI ${confidence}%</p>
                <div style="margin-top:6px;">${statusBadge(report.status)}</div>
              </div>
              ${
                withActions && report.status === "pending"
                  ? `<div class="report-actions" style="display:flex; flex-direction:column; gap:6px;">
                      <button class="small-button" type="button" style="background:var(--green); color:#fff; border:none; padding:4px 8px; border-radius:4px; cursor:pointer;" data-action="approve-report" data-id="${report.id}">${t("approved")}</button>
                      <button class="small-button" type="button" style="background:var(--error); color:#fff; border:none; padding:4px 8px; border-radius:4px; cursor:pointer;" data-action="reject-report" data-id="${report.id}">${t("rejected")}</button>
                    </div>`
                  : ""
              }
            </article>
          `;
        })
        .join("")}
    </div>
  `;
}

function supplierCard(name, rating, complaints, losses) {
  return `
    <article class="supplier-card">
      <strong>${escapeHtml(name)}</strong>
      <p>Rating: <span class="badge ${rating >= 4.5 ? 'badge-approved' : 'badge-pending'}">${rating}/5.0</span></p>
      <p>${complaints} ${t("complaints")}</p>
      <span class="tag" style="display:inline-block; margin-top:6px;">${money(losses)}</span>
    </article>
  `;
}

function renderManager() {
  const managerName = state.profile.fullname || "Bahandi Manager";
  app.innerHTML = `
    <section class="manager-hero glass-panel">
      <div>
        <span class="soft-label">${t("navManagerProfile")}</span>
        <h2>${escapeHtml(managerName)}</h2>
        <p>${t("managerProfileText")}</p>
      </div>
      <button class="primary-button" type="button" data-view="requests" style="width:auto; margin-top:10px;">${t("pendingRequests")} (${state.reports.filter(r => r.status==='pending').length})</button>
    </section>
    <section class="grid four manager-kpis" style="margin-top: 14px;">
      ${metric(t("losses"), money(state.analytics.totalLoss || 0), t("allRequests"))}
      ${metric(t("pending"), state.reports.filter(r=>r.status==='pending').length, t("managerQueue"))}
      ${metric(t("approval"), `${state.analytics.approvalRate || 85}%`, t("approved"))}
      ${metric(t("prevented"), money(state.analytics.preventedLosses || 0), "AI Ops")}
    </section>
    <section class="grid two" style="margin-top:18px">
      <div class="panel active glass-panel">
        <h2>${t("controlCenter")}</h2>
        ${renderManagerProfileCards()}
      </div>
      <div class="panel active glass-panel">
        <h2>${t("rootCause")}</h2>
        ${renderStatusList([
          { title: "AI Daily Advice", value: "FIFO ротация", hint: state.analytics.ai_daily_insight || "Проверьте хранение молочной продукции на точках." },
          { title: "Главный фактор", value: "Списания по просрочке", hint: state.analytics.root_cause_summary || "Основная статья потерь по сети." },
          { title: "AI Прогноз потерь", value: money(state.analytics.forecast_losses_next_month_tenge), hint: "Прогнозируемые потери на следующий месяц." }
        ])}
      </div>
    </section>
  `;
}

function renderRequests() {
  const pending = state.reports.filter((report) => report.status === "pending");
  const approved = state.reports.filter((report) => report.status === "approved");
  app.innerHTML = `
    <section class="grid two">
      <div class="panel active glass-panel">
        <h2>${t("approvalQueue")} (${pending.length})</h2>
        <div style="margin-top:10px;">
          ${pending.length ? renderReportList(pending, true) : `<div class="empty-state">${t("noPending")}</div>`}
        </div>
      </div>
      <div class="panel active glass-panel">
        <h2>${t("approvedTable")}</h2>
        <div style="margin-top:10px;">
          ${approved.length ? renderReportList(approved.slice(0, 8), false) : `<div class="empty-state">${t("historyEmpty")}</div>`}
        </div>
      </div>
    </section>
    <section class="panel active glass-panel" style="margin-top:18px">
      <h2>${t("history")}</h2>
      <div style="margin-top:10px;">
        ${state.reports.length ? renderReportList(state.reports, false) : `<div class="empty-state">${t("historyEmpty")}</div>`}
      </div>
    </section>
  `;
}

function renderHeatMap() {
  return `
    <div class="heat-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 8px;">
      ${state.heatmap.map((b) => {
        const levelClass = b.status_color === "red" ? "high" : b.status_color === "yellow" ? "medium" : "low";
        return `
          <span class="${levelClass}" style="padding: 10px; border-radius: 8px; text-align: center; font-size: 0.85rem; color: #fff;">
            <strong>${escapeHtml(b.branch_name)}</strong>
            <small style="display:block; margin-top:4px;">${money(b.total_losses_tenge)}</small>
          </span>
        `;
      }).join("")}
    </div>
  `;
}

function renderSuppliers() {
  app.innerHTML = `
    <section class="grid two">
      <div class="panel active glass-panel">
        <h2>${t("supplierQuality")}</h2>
        <div class="supplier-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top:10px;">
          ${state.suppliers.map(s => supplierCard(s.name, s.ai_rating, s.complaints, s.losses_tenge)).join("")}
        </div>
      </div>
      <div class="panel active glass-panel">
        <h2>AI supplier advice</h2>
        <div style="margin-top: 10px;">
          ${renderStatusList([
            { title: "FreshFood", value: "Высокий риск потерь", hint: "AI обнаружил частые дефекты упаковки и порчу томатов." },
            { title: "Baker Pro", value: "Стабильно", hint: "Самый высокий AI-рейтинг поставок хлебобулочной продукции." },
            { title: "Qazaq Dairy", value: "Требует внимания", hint: "Поставки стабильные, но участились жалобы на герметичность." }
          ])}
        </div>
      </div>
    </section>
  `;
}

function renderReportsCenter() {
  const periods = [
    ["today", t("pdfToday")],
    ["week", t("pdfWeek")],
    ["month", t("pdfMonth")],
    ["quarter", t("pdfQuarter")],
    ["year", t("pdfYear")],
    ["iiko", t("pdfIiko")]
  ];
  app.innerHTML = `
    <section class="panel active glass-panel">
      <h2>${t("reportsTitle")}</h2>
      <div class="report-period-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 10px; margin-top:12px;">
        ${periods
          .map(
            ([period, label]) => `
              <a class="report-period-card" href="/api/reports/pdf?period=${period}" target="_blank" rel="noreferrer" style="padding:16px; text-decoration:none; border-radius:8px; background:rgba(255,255,255,0.03); display:flex; flex-direction:column; justify-content:center; align-items:center; border:1px solid var(--line);">
                <strong>${escapeHtml(label)}</strong>
                <span style="font-size:0.75rem; color:var(--blue); margin-top:6px;">${t("downloadPdf")}</span>
              </a>
            `
          )
          .join("")}
      </div>
    </section>
    <section class="panel active glass-panel" style="margin-top:18px">
      <h2>${t("approvedTable")}</h2>
      <div style="margin-top: 10px;">
        ${state.reports.length ? renderReportList(state.reports.filter(r => r.status === 'approved'), false) : `<div class="empty-state">${t("historyEmpty")}</div>`}
      </div>
    </section>
  `;
}

function correctionBars() {
  const entries = Object.entries(state.analytics.productCorrections || {}).sort((a, b) => b[1] - a[1]);
  if (!entries.length) return `<div class="empty-state">${t("noCorrections")}</div>`;
  const max = Math.max(...entries.map((entry) => entry[1]), 1);
  return `<div class="bar-list">${entries
    .map(
      ([product, count]) => `
        <div class="bar-row">
          <header><span>${escapeHtml(productLabel(product))}</span><span>${count}</span></header>
          <div class="bar-track"><span style="--width:${Math.round((count / max) * 100)}%"></span></div>
        </div>`
    )
    .join("")}</div>`;
}

function lossBars() {
  const entries = Object.entries(state.analytics.productLosses || {}).sort((a, b) => b[1] - a[1]);
  if (!entries.length) return `<div class="empty-state">${t("noLosses")}</div>`;
  const max = Math.max(...entries.map((entry) => entry[1]), 1);
  return `<div class="bar-list">${entries
    .map(
      ([product, value]) => `
        <div class="bar-row">
          <header><span>${escapeHtml(productLabel(product))}</span><span>${money(value)}</span></header>
          <div class="bar-track"><span style="--width:${Math.round((value / max) * 100)}%"></span></div>
        </div>`
    )
    .join("")}</div>`;
}

function renderAnalytics() {
  app.innerHTML = `
    <section class="grid five">
      ${metric("AI confidence", `${state.analytics.averageConfidence || 0}%`, t("avgConfidence"))}
      ${metric(t("corrections"), state.analytics.employeeCorrections || 0, t("employeeCorrections"))}
      ${metric(t("approval"), `${state.analytics.approvalRate || 0}%`, t("navManager"))}
      ${metric(t("falseDetections"), state.analytics.falseDetections || 0, t("lowOrCorrection"))}
      ${metric(t("objectCount"), state.reports.length, t("allPhotos"))}
    </section>
    <section class="grid two" style="margin-top:18px">
      <div class="panel active"><h2>${t("employeeCorrections")}</h2>${correctionBars()}</div>
      <div class="panel active"><h2>${t("productLosses")}</h2>${lossBars()}</div>
    </section>
    <section class="grid two" style="margin-top:18px">
      <div class="panel active glass-panel"><h2>${t("heatMap")}</h2>${renderHeatMap()}</div>
      <div class="panel active glass-panel"><h2>${t("forecast")}</h2>${renderStatusList([
        { title: "Тренд следующей недели", value: "+12%", hint: "При сохранении текущей интенсивности списаний." },
        { title: "Потенциал оптимизации", value: money(state.analytics.preventedLosses * 1.5), hint: "При обучении персонала стандартам ротации FIFO." },
        { title: "Ложные определения", value: String(state.analytics.falseDetections || 0), hint: t("lowOrCorrection") }
      ])}</div>
    </section>
    <section class="panel active glass-panel" style="margin-top:18px">
      <h2>${t("aiDashboard")}</h2>
      <div class="detection-card">
        <span class="tag">Bahandisation API</span>
        <strong>${t("analyticsText")}</strong>
      </div>
    </section>
  `;
}

function renderExecutive() {
  app.innerHTML = `
    <section class="executive-layout">
      <div class="manager-hero glass-panel" style="display:flex; justify-content:space-between; align-items:center;">
        <div>
          <span class="soft-label">${t("executiveTitle")}</span>
          <h2>${money(state.analytics.totalLoss || 0)}</h2>
          <p>Основной инсайт: ${state.analytics.ai_daily_insight || 'Контролируйте списания на точках в вечернее время.'}</p>
        </div>
        <div style="text-align:right;">
          <span class="soft-label" style="display:block;">Сэкономлено AI</span>
          <strong class="executive-saving" style="font-size:1.8rem; color:var(--green);">${money(state.analytics.preventedLosses || 0)}</strong>
        </div>
      </div>
      <div class="grid three" style="margin-top:14px;">
        ${metric(t("approval"), `${state.analytics.approvalRate || 0}%`, t("approved"))}
        ${metric(t("corrections"), `${state.analytics.correctionRate || 0}%`, t("employeeCorrections"))}
        ${metric(t("forecast"), money(state.analytics.forecast_losses_next_month_tenge), "Прогноз списаний на следующий месяц")}
      </div>
      <section class="grid two" style="margin-top:18px">
        <div class="panel active glass-panel"><h2>${t("heatMap")}</h2>${renderHeatMap()}</div>
        <div class="panel active glass-panel"><h2>${t("rootCause")}</h2>${renderStatusList([
          { title: "Сэкономлено AI", value: money(state.analytics.preventedLosses || 0), hint: "Предотвращенные потери благодаря верификации." },
          { title: "Главный фактор", value: state.analytics.root_cause_summary || "Просрочка", hint: "Наиболее частая причина списаний." },
          { title: "Рекомендация поставщика", value: "FreshFood", hint: "Провести проверку условий транспортировки томатов." }
        ])}</div>
      </section>
    </section>
  `;
}

function render() {
  syncChrome();
  if (!state.role) {
    renderAuth();
    return;
  }
  if (state.view === "employee") renderEmployee();
  if (state.view === "report") renderReport();
  if (state.view === "personal") renderPersonal();
  if (state.view === "manager") renderManager();
  if (state.view === "requests") renderRequests();
  if (state.view === "analytics") renderAnalytics();
  if (state.view === "suppliers") renderSuppliers();
  if (state.view === "reports") renderReportsCenter();
  if (state.view === "executive") renderExecutive();
}

function createSampleImage() {
  const canvas = document.createElement("canvas");
  canvas.width = 640;
  canvas.height = 420;
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#f6f1e7";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#13261d";
  ctx.fillRect(54, 54, 532, 312);
  ctx.fillStyle = "#fffaf0";
  ctx.fillRect(74, 74, 492, 272);
  ctx.fillStyle = "#d69c32";
  for (let i = 0; i < 18; i += 1) {
    const x = 112 + (i % 9) * 22;
    const y = 112 + Math.floor(i / 9) * 34;
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate((i % 5) * 0.16);
    ctx.fillRect(-5, -38, 10, 88);
    ctx.restore();
  }
  return canvas.toDataURL("image/png");
}

function useSampleImage() {
  state.image = createSampleImage();
  state.imageName = "demo-food-tray.png";
  state.detection = null;
  state.draftId = "";
  setView("report");
  window.setTimeout(analyzeImage, 0);
}

async function handleFile(file) {
  if (!file) return;
  if (file.size > 8 * 1024 * 1024) {
    showToast(t("fileLarge"));
    return;
  }
  const reader = new FileReader();
  reader.onload = () => {
    state.image = String(reader.result || "");
    state.imageName = file.name;
    state.detection = null;
    state.draftId = "";
    render();
    analyzeImage();
  };
  reader.readAsDataURL(file);
}

// Perform image analysis using Roboflow scanning API
async function analyzeImage() {
  if (!state.image) {
    showToast(t("addPhotoToAnalyze"));
    return;
  }
  state.loading = true;
  render();
  try {
    const fd = new FormData();
    const fileInput = document.getElementById("imageInput");
    const file = fileInput ? fileInput.files[0] : null;
    
    if (file) {
      fd.append("photo", file);
    } else {
      // Convert base64 demo photo back to blob
      const res = await fetch(state.image);
      const blob = await res.blob();
      fd.append("photo", blob, state.imageName || "demo.png");
    }

    const result = await api("/api/worker/write-off/scan/", {
      method: "POST",
      body: fd
    });

    if (result.success) {
      state.detection = {
        source: result.source || "Roboflow Live",
        detectedProduct: result.product_name,
        productId: result.product_id,
        quantity: 1,
        confidence: Math.round(result.confidence || 93),
        boundingBoxes: [{}]
      };
      // Bind to form
      state.form.product = result.product_id;
      state.form.quantity = 1;
      showToast(t("aiReady"));
    } else {
      throw new Error(result.error || "Failed to scan image");
    }
  } catch (error) {
    console.error("Scanning error:", error);
    state.detection = {
      source: "manual_fallback",
      detectedProduct: "",
      productId: "",
      quantity: 1,
      confidence: 0,
      boundingBoxes: []
    };
    showToast(t("aiUnavailable"));
  } finally {
    state.loading = false;
    render();
  }
}

function confirmDetection() {
  if (!state.detection) return;
  if (state.detection.productId) state.form.product = state.detection.productId;
  if (state.detection.quantity) state.form.quantity = state.detection.quantity;
  showToast(t("aiConfirmed"));
  render();
}

function enableManualMode() {
  state.detection = state.detection || {
    source: "manual",
    confidence: 0,
    detectedProduct: "",
    productId: "",
    quantity: state.form.quantity,
    boundingBoxes: []
  };
  showToast(t("manualEnabled"));
  render();
}

// Submit a new write-off report to Django backend
async function submitReport() {
  if (!state.image) {
    showToast(t("addPhoto"));
    return;
  }
  if (!state.form.product) {
    showToast(t("chooseProduct"));
    return;
  }
  if (String(state.form.comment || "").trim().length < 10) {
    showToast(t("commentMin"));
    return;
  }
  state.submitting = true;
  render();
  try {
    const fd = new FormData();
    fd.append("product", state.form.product);
    fd.append("quantity", state.form.quantity);
    fd.append("reason", state.form.reason);
    fd.append("ai_confidence", state.detection ? (state.detection.confidence || 0) : 0);
    
    // Attach comment inside reason/notes if needed or as reason fallback
    // Since Django model doesn't explicitly store comment, we append it to notes or ignore.
    
    const fileInput = document.getElementById("imageInput");
    const file = fileInput ? fileInput.files[0] : null;
    if (file) {
      fd.append("photo", file);
    } else {
      const res = await fetch(state.image);
      const blob = await res.blob();
      fd.append("photo", blob, state.imageName || "writeoff.png");
    }

    await api("/api/worker/write-off/create/", {
      method: "POST",
      body: fd
    });

    // Clear report state
    state.image = "";
    state.imageName = "";
    state.detection = null;
    state.form.product = "";
    state.form.quantity = 1;
    state.form.comment = "";
    
    await refreshData();
    setView("employee");
    showToast(t("reportSent"));
  } catch (error) {
    console.error("Submit error:", error);
    showToast("Ошибка отправки: " + error.message);
  } finally {
    state.submitting = false;
    render();
  }
}

// Approve or reject a report from manager review screen
async function updateReportStatus(id, actionStatus) {
  try {
    await api(`/api/manager/requests/${id}/review/`, {
      method: "PATCH",
      body: JSON.stringify({ action: actionStatus })
    });
    await refreshData();
    render();
    showToast(actionStatus === "approve" ? t("approvedToast") : t("rejectedToast"));
  } catch (error) {
    console.error("Review status error:", error);
    showToast("Ошибка обновления статуса: " + error.message);
  }
}

function updateField(field, value) {
  if (field === "quantity") {
    state.form.quantity = Math.max(1, Number(value || 1));
    return;
  }
  state.form[field] = value;
  if (field === "branchId") {
    const store = state.stores.find((item) => item.id == value);
    state.form.branchName = store?.name || "";
  }
}

function updateBurgerScene() {
  const maxScroll = Math.max(1, window.innerHeight * 0.9);
  const progress = Math.max(0, Math.min(1, window.scrollY / maxScroll));
  document.documentElement.style.setProperty("--burger-progress", progress.toFixed(3));
  document.documentElement.style.setProperty("--burger-rotate", `${Math.round(progress * 38)}deg`);
}

function logout() {
  localStorage.removeItem("bh_token");
  localStorage.removeItem("bh_refresh");
  localStorage.removeItem("bh_role");
  localStorage.removeItem("bh_uname");
  localStorage.removeItem("bh_fname");
  
  TOKEN = REFRESH = state.role = "";
  state.auth.email = "";
  state.auth.password = "";
  setView("employee");
}

// Interactive lightbox for photos
window.openLB = function(src) {
  const lb = document.createElement("div");
  lb.style = "position:fixed; inset:0; z-index:9999; background:rgba(0,0,0,0.85); display:grid; place-items:center; cursor:zoom-out;";
  lb.innerHTML = `<img src="${src}" style="max-width:90%; max-height:90%; border-radius:8px; box-shadow:0 10px 40px rgba(0,0,0,0.5);" />`;
  lb.onclick = () => lb.remove();
  document.body.appendChild(lb);
};

window.addEventListener("scroll", updateBurgerScene, { passive: true });

document.addEventListener("click", (event) => {
  const viewButton = event.target.closest("[data-view]");
  if (viewButton) {
    setView(viewButton.dataset.view);
    return;
  }
  const reasonButton = event.target.closest("[data-reason]");
  if (reasonButton) {
    state.form.reason = reasonButton.dataset.reason;
    state.reasonOpen = false;
    render();
    return;
  }
  const actionButton = event.target.closest("[data-action]");
  if (!actionButton) return;
  const action = actionButton.dataset.action;

  if (action === "choose-auth-role") {
    state.authRole = actionButton.dataset.role || "employee";
    render();
    return;
  }
  if (action === "enter-selected-role") {
    const emailInput = document.querySelector('[data-auth-field="email"]');
    const passwordInput = document.querySelector('[data-auth-field="password"]');
    const emailVal = emailInput ? emailInput.value.trim() : "";
    const passwordVal = passwordInput ? passwordInput.value : "";

    if (!emailVal || !passwordVal) {
      showToast(t("authMissing"));
      return;
    }

    state.loading = true;
    render();

    // Call authentication Django simple-jwt endpoint
    fetch(API_URL + "/api/auth/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username: emailVal, password: passwordVal })
    })
      .then((res) => {
        if (!res.ok) throw new Error("Неверный логин или пароль");
        return res.json();
      })
      .then((data) => {
        TOKEN = data.access;
        REFRESH = data.refresh;
        state.role = data.role === 'admin' ? 'manager' : data.role; // map admin/manager to manager flow
        
        localStorage.setItem("bh_token", TOKEN);
        localStorage.setItem("bh_refresh", REFRESH);
        localStorage.setItem("bh_role", state.role);
        localStorage.setItem("bh_uname", data.username);
        localStorage.setItem("bh_fname", data.fullname);
        
        showToast("Авторизация успешна!");
        setView(state.role === "manager" ? "manager" : "employee");
        refreshData();
      })
      .catch((err) => {
        showToast(err.message);
      })
      .finally(() => {
        state.loading = false;
        render();
      });
    return;
  }
  if (action === "logout") {
    logout();
    return;
  }
  if (action === "toggle-reason") {
    state.reasonOpen = !state.reasonOpen;
    render();
    return;
  }
  if (action === "open-report") setView("report");
  if (action === "sample-report" || action === "use-sample") useSampleImage();
  if (action === "clear-image") {
    state.image = "";
    state.imageName = "";
    state.detection = null;
    state.draftId = "";
    render();
  }
  if (action === "analyze") analyzeImage();
  if (action === "confirm-detection") confirmDetection();
  if (action === "edit-detection" || action === "manual-mode") enableManualMode();
  
  if (action === "inc-qty") {
    state.form.quantity += 1;
    render();
  }
  if (action === "dec-qty") {
    state.form.quantity = Math.max(1, state.form.quantity - 1);
    render();
  }
  if (action === "submit-report") submitReport();
  
  if (action === "approve-report") updateReportStatus(actionButton.dataset.id, "approve");
  if (action === "reject-report") updateReportStatus(actionButton.dataset.id, "reject");
});

document.addEventListener("change", (event) => {
  if (event.target.id === "imageInput") {
    handleFile(event.target.files?.[0]);
    return;
  }
  if (event.target.id === "languageSelect") {
    state.language = event.target.value;
    localStorage.setItem("wasteiq-language", state.language);
    syncChrome();
    render();
    return;
  }
  const input = event.target.closest("[data-field]");
  if (input) {
    updateField(input.dataset.field, input.value);
  }
});

// App Initialization
document.addEventListener("DOMContentLoaded", () => {
  syncChrome();
  if (TOKEN && state.role) {
    setView(state.role === "manager" ? "manager" : "employee");
    refreshData();
  } else {
    render();
  }
});
