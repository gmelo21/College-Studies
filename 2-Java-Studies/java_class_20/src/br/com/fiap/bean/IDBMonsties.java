package br.com.fiap.bean;

import java.io.IOException;

public interface IDBMonsties {
    void record(String path) throws IOException;
    Monsties read(String path) throws IOException;
}
