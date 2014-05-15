class ErrorCodes(object):
    """
    A set of constants representing validation errors.  Validation error messages can change, but the codes will not.
    See the source for a list of all errors codes.

    Codes can be used to check for specific validation errors::

        result = Transaction.sale({})
        assert(result.is_success == False)
        assert(result.errors.for_object("transaction").on("amount")[0].code == ErrorCodes.Transaction.AmountIsRequired)
    """

    class Address(object):
        CannotBeBlank = "81801"
        CompanyIsInvalid = "91821"
        CompanyIsTooLong = "81802"
        CountryCodeAlpha2IsNotAccepted = "91814"
        CountryCodeAlpha3IsNotAccepted = "91816"
        CountryCodeNumericIsNotAccepted = "91817"
        CountryNameIsNotAccepted = "91803"
        ExtedAddressIsTooLong = "81804" # Deprecated
        ExtendedAddressIsInvalid = "91823"
        ExtendedAddressIsTooLong = "81804"
        FirstNameIsInvalid = "91819"
        FirstNameIsTooLong = "81805"
        InconsistentCountry = "91815"
        LastNameIsInvalid = "91820"
        LastNameIsTooLong = "81806"
        LocalityIsInvalid = "91824"
        LocalityIsTooLong = "81807"
        PostalCodeInvalidCharacters = "81813"
        PostalCodeIsInvalid = "91826"
        PostalCodeIsRequired = "81808"
        PostalCodeIsTooLong = "81809"
        RegionIsInvalid = "91825"
        RegionIsTooLong = "81810"
        StreetAddressIsInvalid = "91822"
        StreetAddressIsRequired = "81811"
        StreetAddressIsTooLong = "81812"
        TooManyAddressesPerCustomer = "91818"

    class CreditCard(object):
        BillingAddressConflict = "91701"
        BillingAddressIdIsInvalid = "91702"
        CardholderNameIsTooLong = "81723"
        CreditCardTypeIsNotAccepted = "81703"
        CreditCardTypeIsNotAcceptedBySubscriptionMerchantAccount = "81718"
        CustomerIdIsInvalid = "91705"
        CustomerIdIsRequired = "91704"
        CvvIsInvalid = "81707"
        CvvIsRequired = "81706"
        DuplicateCardExists = "81724"
        ExpirationDateConflict = "91708"
        ExpirationDateIsInvalid = "81710"
        ExpirationDateIsRequired = "81709"
        ExpirationDateYearIsInvalid = "81711"
        ExpirationMonthIsInvalid = "81712"
        ExpirationYearIsInvalid = "81713"
        InvalidVenmoSDKPaymentMethodCode = "91727"
        NumberHasInvalidLength = NumberLengthIsInvalid = "81716"
        NumberIsInvalid = "81715"
        NumberIsRequired = "81714"
        NumberMustBeTestNumber = "81717"
        PaymentMethodConflict = "81725"
        TokenInvalid = TokenFormatIsInvalid = "91718"
        TokenIsInUse = "91719"
        TokenIsNotAllowed = "91721"
        TokenIsRequired = "91722"
        TokenIsTooLong = "91720"
        VenmoSDKPaymentMethodCodeCardTypeIsNotAccepted = "91726"
        VerificationNotSupportedOnThisMerchantAccount = "91730"

        class Options(object):
            UpdateExistingTokenIsInvalid = "91723"
            VerificationMerchantAccountIdIsInvalid = "91728"
            UpdateExistingTokenNotAllowed = "91729"


    class Customer(object):
        CompanyIsTooLong = "81601"
        CustomFieldIsInvalid = "91602"
        CustomFieldIsTooLong = "81603"
        EmailIsInvalid = EmailFormatIsInvalid = "81604"
        EmailIsRequired = "81606"
        EmailIsTooLong = "81605"
        FaxIsTooLong = "81607"
        FirstNameIsTooLong = "81608"
        IdIsInUse = "91609"
        IdIsInvaild = "91610" # Deprecated
        IdIsInvalid = "91610"
        IdIsNotAllowed = "91611"
        IdIsRequired = "91613"
        IdIsTooLong = "91612"
        LastNameIsTooLong = "81613"
        PhoneIsTooLong = "81614"
        WebsiteIsInvalid = WebsiteFormatIsInvalid = "81616"
        WebsiteIsTooLong = "81615"

    class Descriptor(object):
        DynamicDescriptorsDisabled = "92203"
        InternationalNameFormatIsInvalid = "92204"
        InternationalPhoneFormatIsInvalid = "92205"
        NameFormatIsInvalid = "92201"
        PhoneFormatIsInvalid = "92202"

    class MerchantAccount(object):
        IdFormatIsInvalid = "82603"
        IdIsInUse = "82604"
        IdIsNotAllowed = "82605"
        IdIsTooLong = "82602"
        MasterMerchantAccountIdIsInvalid = "82607"
        MasterMerchantAccountIdIsRequired = "82606"
        MasterMerchantAccountMustBeActive = "82608"
        TosAcceptedIsRequired = "82610"
        CannotBeUpdated = "82674"
        IdCannotBeUpdated = "82675"
        MasterMerchantAccountIdCannotBeUpdated = "82676"
        Declined = "82626"
        DeclinedMasterCardMatch = "82622"
        DeclinedOFAC = "82621"
        DeclinedFailedKYC = "82623"
        DeclinedSsnInvalid = "82624"
        DeclinedSsnMatchesDeceased = "82625"

        class ApplicantDetails(object):
            AccountNumberIsRequired = "82614"
            CompanyNameIsInvalid = "82631"
            CompanyNameIsRequiredWithTaxId = "82633"
            DateOfBirthIsRequired = "82612"
            Declined = "82626" # Keep for backwards compatibility
            DeclinedMasterCardMatch = "82622" # Keep for backwards compatibility
            DeclinedOFAC = "82621" # Keep for backwards compatibility
            DeclinedFailedKYC = "82623" # Keep for backwards compatibility
            DeclinedSsnInvalid = "82624" # Keep for backwards compatibility
            DeclinedSsnMatchesDeceased = "82625" # Keep for backwards compatibility
            EmailAddressIsInvalid = "82616"
            FirstNameIsInvalid = "82627"
            FirstNameIsRequired = "82609"
            LastNameIsInvalid = "82628"
            LastNameIsRequired = "82611"
            PhoneIsInvalid = "82636"
            RoutingNumberIsInvalid = "82635"
            RoutingNumberIsRequired = "82613"
            SsnIsInvalid = "82615"
            TaxIdIsInvalid = "82632"
            TaxIdIsRequiredWithCompanyName = "82634"
            DateOfBirthIsInvalid = "82663"
            EmailAddressIsRequired = "82665"
            AccountNumberIsInvalid = "82670"
            TaxIdMustBeBlank = "82673"

            class Address(object):
                LocalityIsRequired = "82618"
                PostalCodeIsInvalid = "82630"
                PostalCodeIsRequired = "82619"
                RegionIsRequired = "82620"
                StreetAddressIsInvalid = "82629"
                StreetAddressIsRequired = "82617"
                RegionIsInvalid = "82664"

        class Individual(object):
            FirstNameIsRequired = "82637"
            LastNameIsRequired = "82638"
            DateOfBirthIsRequired = "82639"
            SsnIsInvalid = "82642"
            EmailAddressIsInvalid = "82643"
            FirstNameIsInvalid = "82644"
            LastNameIsInvalid = "82645"
            PhoneIsInvalid = "82656"
            DateOfBirthIsInvalid = "82666"
            EmailAddressIsRequired = "82667"

            class Address(object):
                StreetAddressIsRequired = "82657"
                LocalityIsRequired = "82658"
                PostalCodeIsRequired = "82659"
                RegionIsRequired = "82660"
                StreetAddressIsInvalid = "82661"
                PostalCodeIsInvalid = "82662"
                RegionIsInvalid = "82668"

        class Business(object):
            DbaNameIsInvalid = "82646"
            LegalNameIsInvalid = "82677"
            LegalNameIsRequiredWithTaxId = "82669"
            TaxIdIsInvalid = "82647"
            TaxIdIsRequiredWithLegalName = "82648"
            TaxIdMustBeBlank = "82672"
            class Address(object):
                StreetAddressIsInvalid = "82685"
                PostalCodeIsInvalid = "82686"
                RegionIsInvalid = "82684"

        class Funding(object):
            RoutingNumberIsRequired = "82640"
            AccountNumberIsRequired = "82641"
            RoutingNumberIsInvalid = "82649"
            AccountNumberIsInvalid = "82671"
            DestinationIsInvalid = "82679"
            DestinationIsRequired = "82678"
            EmailAddressIsInvalid = "82681"
            EmailAddressIsRequired = "82680"
            MobilePhoneIsInvalid = "82683"
            MobilePhoneIsRequired = "82682"

    class PaymentMethod(object):
        PaymentMethodParamsAreRequired = "93101"
        NonceIsInvalid = "93102"
        NonceIsRequired = "93103"
        CustomerIdIsRequired = "93104"
        CustomerIdIsInvalid = "93105"

    class PayPalAccount(object):
        ConsentCodeOrAccessTokenIsRequired = "82901"
        CannotVaultOneTimeUsePayPalAccount = "82902"
        CannotHaveBothAccessTokenAndConsentCode = "82903"
        PayPalAccountsAreNotAccepted = "82904"
        CustomerIdIsRequiredForVaulting = "82905"
        TokenIsInUse = "92906"
        PaymentMethodNonceConsumed = "92907"
        PaymentMethodNonceUnknown = "92908"
        PaymentMethodNonceLocked = "92909"

    class SettlementBatchSummary(object):
        CustomFieldIsInvalid = "82303"
        SettlementDateIsInvalid = "82302"
        SettlementDateIsRequired = "82301"

    class Subscription(object):
        BillingDayOfMonthCannotBeUpdated = "91918"
        BillingDayOfMonthIsInvalid = "91914"
        BillingDayOfMonthMustBeNumeric = "91913"
        CannotAddDuplicateAddonOrDiscount = "91911"
        CannotEditCanceledSubscription = "81901"
        CannotEditExpiredSubscription = "81910"
        CannotEditPriceChangingFieldsOnPastDueSubscription = "91920"
        FirstBillingDateCannotBeInThePast = "91916"
        FirstBillingDateCannotBeUpdated = "91919"
        FirstBillingDateIsInvalid = "91915"
        IdIsInUse = "81902"
        InconsistentNumberOfBillingCycles = "91908"
        InconsistentStartDate = "91917"
        InvalidRequestFormat = "91921"
        MerchantAccountIdIsInvalid = "91901"
        MismatchCurrencyISOCode = "91923"
        NumberOfBillingCyclesCannotBeBlank = "91912"
        NumberOfBillingCyclesIsTooSmall = "91909"
        NumberOfBillingCyclesMustBeGreaterThanZero = "91907"
        NumberOfBillingCyclesMustBeNumeric = "91906"
        PaymentMethodTokenCardTypeIsNotAccepted = "91902"
        PaymentMethodTokenIsInvalid = "91903"
        PaymentMethodTokenNotAssociatedWithCustomer = "91905"
        PlanBillingFrequencyCannotBeUpdated = "91922"
        PlanIdIsInvalid = "91904"
        PriceCannotBeBlank = "81903"
        PriceFormatIsInvalid = "81904"
        PriceIsTooLarge = "81923"
        StatusIsCanceled = "81905"
        TokenFormatIsInvalid = "81906"
        TrialDurationFormatIsInvalid = "81907"
        TrialDurationIsRequired = "81908"
        TrialDurationUnitIsInvalid = "81909"

        class Modification(object):
            AmountCannotBeBlank = "92003"
            AmountIsInvalid = "92002"
            AmountIsTooLarge = "92023"
            CannotEditModificationsOnPastDueSubscription = "92022"
            CannotUpdateAndRemove = "92015"
            ExistingIdIsIncorrectKind = "92020"
            ExistingIdIsInvalid = "92011"
            ExistingIdIsRequired = "92012"
            IdToRemoveIsIncorrectKind = "92021"
            IdToRemoveIsNotPresent = "92016"
            InconsistentNumberOfBillingCycles = "92018"
            InheritedFromIdIsInvalid = "92013"
            InheritedFromIdIsRequired = "92014"
            Missing = "92024"
            NumberOfBillingCyclesCannotBeBlank = "92017"
            NumberOfBillingCyclesIsInvalid = "92005"
            NumberOfBillingCyclesMustBeGreaterThanZero = "92019"
            QuantityCannotBeBlank = "92004"
            QuantityIsInvalid = "92001"
            QuantityMustBeGreaterThanZero = "92010"

    class Transaction(object):
        AmountCannotBeNegative = "81501"
        AmountIsInvalid = AmountFormatIsInvalid = "81503"
        AmountIsRequired = "81502"
        AmountIsTooLarge = "81528"
        AmountMustBeGreaterThanZero = "81531"
        BillingAddressConflict = "91530"
        CannotBeVoided = "91504"
        CannotCancelRelease = "91562"
        CannotCloneCredit = "91543"
        CannotCloneTransactionWithVaultCreditCard = "91540"
        CannotCloneUnsuccessfulTransaction = "91542"
        CannotCloneVoiceAuthorizations = "91541"
        CannotHoldInEscrow = "91560"
        CannotPartiallyRefundEscrowedTransaction = "91563"
        CannotRefundCredit = "91505"
        CannotRefundUnlessSettled = "91506"
        CannotRefundWithPendingMerchantAccount = "91559"
        CannotRefundWithSuspendedMerchantAccount = "91538"
        CannotReleaseFromEscrow = "91561"
        CannotSubmitForSettlement = "91507"
        ChannelIsTooLong = "91550"
        ChannelIsTooLong = "91550"
        CreditCardIsRequired = "91508"
        CustomFieldIsInvalid = "91526"
        CustomFieldIsTooLong = "81527"
        CustomerDefaultPaymentMethodCardTypeIsNotAccepted = "81509"
        CustomerDoesNotHaveCreditCard = "91511"
        CustomerIdIsInvalid = "91510"
        HasAlreadyBeenRefunded = "91512"
        MerchantAccountDoesNotSupportMOTO = "91558"
        MerchantAccountDoesNotSupportRefunds = "91547"
        MerchantAccountIdIsInvalid = "91513"
        MerchantAccountIsSusped = "91514" # Deprecated
        MerchantAccountIsSuspended = "91514"
        MerchantAccountNameIsInvalid = "91513" # Deprecated
        OrderIdIsTooLong = "91501"
        PaymentMethodConflict = "91515"
        PaymentMethodConflictWithVenmoSDK = "91549"
        PaymentMethodDoesNotBelongToCustomer = "91516"
        PaymentMethodDoesNotBelongToSubscription = "91527"
        PaymentMethodTokenCardTypeIsNotAccepted = "91517"
        PaymentMethodTokenIsInvalid = "91518"
        PaymentMethodNonceUnknown = "91565"
        ProcessorAuthorizationCodeCannotBeSet = "91519"
        ProcessorAuthorizationCodeIsInvalid = "81520"
        ProcessorDoesNotSupportCredits = "91546"
        ProcessorDoesNotSupportVoiceAuthorizations = "91545"
        PurchaseOrderNumberIsInvalid = "91548"
        PurchaseOrderNumberIsTooLong = "91537"
        RefundAmountIsTooLarge = "91521"
        ServiceFeeAmountCannotBeNegative = "91554"
        ServiceFeeAmountFormatIsInvalid = "91555"
        ServiceFeeAmountIsTooLarge = "91556"
        ServiceFeeAmountNotAllowedOnMasterMerchantAccount = "91557"
        ServiceFeeIsNotAllowedOnCredits = "91552"
        SettlementAmountIsLessThanServiceFeeAmount = "91551"
        SettlementAmountIsTooLarge = "91522"
        SubMerchantAccountRequiresServiceFeeAmount = "91553"
        SubscriptionDoesNotBelongToCustomer = "91529"
        SubscriptionIdIsInvalid = "91528"
        SubscriptionStatusMustBePastDue = "91531"
        TaxAmountCannotBeNegative = "81534"
        TaxAmountFormatIsInvalid = "81535"
        TaxAmountIsTooLarge = "81536"
        TypeIsInvalid = "91523"
        TypeIsRequired = "91524"
        UnsupportedVoiceAuthorization = "91539"

        class Options(object):
            VaultIsDisabled = "91525"
            SubmitForSettlementIsRequiredForCloning = "91544"

