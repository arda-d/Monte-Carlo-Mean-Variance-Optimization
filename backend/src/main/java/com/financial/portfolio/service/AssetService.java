package com.financial.portfolio.service;

import com.financial.portfolio.model.Asset;
import com.financial.portfolio.repository.AssetRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
@Service
public class AssetService{
    private final AssetRepository assetRepository;

    //Constructor Injection
    public AssetService(AssetRepository assetRepository) {
        this.assetRepository = assetRepository;
    }

    //Save new asset
    public Asset saveAsset(Asset asset)
    {
        return (Asset) assetRepository.save(asset);
    }

    //List all assets
    public List<Asset> findAllAssets()
    {
        return (List<Asset>) assetRepository.findAll();
    }

    @Transactional
    public List<Asset> saveAllAssets(List<Asset> assets) {
        assetRepository.deleteAll();
        return assetRepository.saveAll(assets);
    }

}
