package com.example.pysidecar;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.sidecar.EnableSidecar;
import org.springframework.cloud.openfeign.EnableFeignClients;

@EnableSidecar
@SpringBootApplication
public class PySidecarApplication {

	public static void main(String[] args) {
		SpringApplication.run(PySidecarApplication.class, args);
	}
}
