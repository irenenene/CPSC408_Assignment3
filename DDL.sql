#DDL

CREATE TABLE Operators (OperatorID integer NOT NULL AUTO_INCREMENT,
                        FirstName varchar(20),
                        LastName varchar(20),
                        PRIMARY KEY (OperatorID));

CREATE TABLE Customers (CustomerID integer NOT NULL AUTO_INCREMENT,
                        CustomerName varchar(50),
                        PrimaryAddress varchar(100),
                        PRIMARY KEY (CustomerID));

CREATE TABLE Batches (BatchID integer NOT NULL AUTO_INCREMENT,
                        WorkstationName varChar(20),
                        BatchType varChar(10),
                        OperatorID integer,
                        CreateTime datetime,
                        ReleaseTime datetime,
                        IsPaper boolean,
                        CustomerID integer,

                        PRIMARY KEY (BatchID),
                        FOREIGN KEY (CustomerID)
                            REFERENCES Customers(CustomerID),
                        FOREIGN KEY (OperatorID)
                            REFERENCES Operators(OperatorID));

CREATE TABLE Suppliers (SupplierID varChar(20) NOT NULL,
                        SupplierName varChar(50),
                        SupplierAddress varChar(100),
                        PRIMARY KEY (SupplierID));

CREATE TABLE Companies (CompanyID varChar(20) NOT NULL,
                        CompanyName varChar(50),
                        CompanyAddress varChar(100),
                        CustomerID integer,
                        PRIMARY KEY (CompanyID),
                        FOREIGN KEY (CustomerID)
                            REFERENCES Customers(CustomerID));

CREATE TABLE Documents (DocumentID integer NOT NULL,
                        BatchID integer NOT NULL,
                        InvoiceNumber varChar(30),
                        InvoiceDate datetime,
                        InvoiceTotal decimal,
                        PurchaseOrderNumber varchar(20),
                        SupplierID varChar(20),
                        CompanyID varChar(20),
                        
                        PRIMARY KEY (DocumentID, BatchID),
                        FOREIGN KEY (BatchID)
                            REFERENCES Batches(BatchID),
                        FOREIGN KEY (SupplierID)
                            REFERENCES Suppliers(SupplierID),
                        FOREIGN KEY (CompanyID)
                            REFERENCES Companies(CompanyID));






